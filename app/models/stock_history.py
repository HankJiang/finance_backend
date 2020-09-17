from app import db


class StockHistory(db.Model):
    __tablename__ = 'stock_history'

    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.ForeignKey('stocks.id'))
    trade_date = db.Column(db.Date())

    open = db.Column(db.Float(2))
    close = db.Column(db.Float(2))
    high = db.Column(db.Float(2))
    low = db.Column(db.Float(2))

    pre_close = db.Column(db.Float(2))
    change = db.Column(db.Float(2))
    change_percent = db.Column(db.Float(2))

    def __init__(self, stock_id, trade_date, open, close, high, low, pre_close, change, change_percent):
        self.stock_id = stock_id
        self.trade_date = trade_date
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.pre_close = pre_close
        self.change = change
        self.change_percent = change_percent

    def __repr__(self):
        return '<Stock %r>' % self.trade_date
