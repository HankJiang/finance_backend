import re
import pandas_datareader as pdr
from flask import json
from enum import Enum
from datetime import datetime

from .base import *


class Stock(BaseModel):
    class MarketChoices(Enum):
        UNKNOWN = 0
        SHANG_HAI = 1
        SHEN_ZHEN = 2

    code = CharField(unique=True)  # 股票唯一编码
    name = CharField()  # 上市公司名称
    market = EnumField(choices=MarketChoices)  # 所属市场

    @classmethod
    def update_by_code(cls, code, history):
        _, market = cls.parse_stock_code(code)
        stock, _ = cls.get_or_create(code=code, market=market)

        for item in history:
            stock.stock_history.model.get_or_create(
                date=item['Date'],
                stock=stock,
                defaults={
                    'close': item['Close'],
                    'high': item['High'],
                    'low': item['Low'],
                    'open': item['Open']
            })

    @classmethod
    def history(cls, code, start, end):
        return cls.search_from_pandas(code, start, end)

    @classmethod
    def realtime(cls, code):
        today = datetime.now().strftime('%Y-%m-%d')
        return cls.search_from_pandas(code, today, today)[0]

    @classmethod
    def search_from_pandas(cls, code, start, end):
        resp = pdr.get_data_yahoo(cls.parse_stock_code(code)[0], start, end)
        data = resp.to_json(orient="table")
        data = json.loads(data)['data']
        data = sorted(data, key=lambda d: d['Date'])
        return data

    @classmethod
    def parse_stock_code(cls, code):
        if re.match('^[00|200|300]', code):
            suffixed, market = code + '.sz', cls.MarketChoices.SHEN_ZHEN
        else:
            suffixed, market = code + '.ss', cls.MarketChoices.SHANG_HAI

        return suffixed, market

