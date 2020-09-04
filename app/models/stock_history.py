from .base import *
from .stock import Stock


class StockHistory(BaseModel):
    stock = ForeignKeyField(Stock, backref='stock_history')  # 股票id
    date = DateField()  # 日期
    high = FloatField()  # 最高
    low = FloatField()  # 最低
    open = FloatField()  # 开盘
    close = FloatField()  # 收盘
