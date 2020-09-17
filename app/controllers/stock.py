from flask import Blueprint
from datetime import datetime
import re

from app.common.api_tools import render_ok, params
from app.services import stock_cli

bp = Blueprint('stock', __name__, url_prefix='/stock')


@bp.route('/', methods=['get'])
def stock():
    data = stock_cli.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    return render_ok(data.to_dict('record'))


@bp.route('/<string:code>', methods=['get'])
def stock_by_code(code):
    data = stock_cli.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

    stock = list(filter(lambda stock: stock['symbol'] == code, data.to_dict('record')))[0]
    return render_ok(stock)


@bp.route('/<string:code>/history', methods=['get'])
def history_by_code(code):
    start, end = params('start', 'end')
    data = stock_cli.daily(ts_code=parse_code(code), start_date=parse_time(start), end_date=parse_time(end))
    data = sorted(data.to_dict('record'), key=lambda d: d['trade_date'])
    return render_ok(data)


def parse_time(t):
    return datetime.strptime(t, '%Y-%m-%d').strftime('%Y%m%d')


def parse_code(code):
    if re.match('^[00|200|300]', code):
        search_code = code + '.SZ'
    else:
        search_code = code + '.SS'

    return search_code
