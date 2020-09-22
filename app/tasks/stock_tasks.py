from datetime import datetime, timedelta
from time import sleep

from app import celery
from app.common.logger_tools import time_log
from app.services.stock_service import stock_cli
from app.models import Stock, StockHistory
from app.common.db_tools import get_or_create
from app import db


@celery.task(name='load_stock')
@time_log
def load_stock():
    data = stock_cli.query('stock_basic', exchange='', list_status='L',
                           fields='ts_code,symbol,name,area,industry,list_date')
    data = data.to_dict('record')

    for item in data:
        get_or_create(db.session, Stock, {'code': item['symbol']},
                      {
                          'search_code': item['ts_code'],
                          'name': item['name'],
                          'area': item['area'],
                          'industry': item['industry'],
                          'ipo_date': item['list_date']
                      }, save=False)

    db.session.commit()


@celery.task(name='load_stock_history')
@time_log
def load_stock_history():
    start = '20170101'
    end = datetime.now().strftime('%Y%m%d')

    i = 0

    for stock in db.session.query(Stock):
        sleep(0.2)
        i += 1
        print(i)

        last_history = db.session.query(StockHistory)\
            .filter_by(stock_id=stock.id)\
            .order_by(StockHistory.trade_date.desc()).first()

        if last_history:
            last_day = last_history.trade_date
            _start = (last_day + timedelta(days=1)).strftime('%Y%m%d')

            items = stock_cli.daily(ts_code=stock.search_code, start_date=_start, end_date=end).to_dict('record')
        else:
            items = stock_cli.daily(ts_code=stock.search_code, start_date=start, end_date=end).to_dict('record')

        if items:
            for item in items:
                history = StockHistory(
                    stock_id=stock.id,
                    trade_date=item['trade_date'],
                    open=item['open'],
                    close=item['close'],
                    high=item['high'],
                    low=item['low'],
                    pre_close=item['pre_close'],
                    change=item['change'],
                    change_percent=item['pct_chg']
                )

                stock.stock_history.append(history)

            db.session.commit()





