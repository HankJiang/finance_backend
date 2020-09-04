from .base import *


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
