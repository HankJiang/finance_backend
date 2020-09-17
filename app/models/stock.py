from app import db


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True)
    search_code = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120), unique=True)

    area = db.Column(db.String(120))
    industry = db.Column(db.String(120))
    ipo_date = db.Column(db.Date())

    def __init__(self, code, search_code, name, area, industry, ipo_date):
        self.code = code
        self.search_code = search_code
        self.name = name
        self.area = area
        self.industry = industry
        self.ipo_date = ipo_date

    def __repr__(self):
        return '<Stock %r>' % self.name



