from peewee import *
from app.db import db


class BaseModel(Model):
    class Meta:
        database = db


# Custom Fields
class EnumField(IntegerField):
    def __init__(self, choices, *args, **kwargs):
        super(IntegerField, self).__init__(*args, **kwargs)
        self.choices = choices

    def db_value(self, value):
        return value.value

    def python_value(self, value):
        return self.choices(value)