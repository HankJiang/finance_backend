import os
from flask import Config


class Development(Config):
    DEBUG = True
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = '127.0.0.1'
    MYSQL_DATABASE_PORT = 3333
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'


class Production(Config):
    DEBUG = False
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = '127.0.0.1'
    MYSQL_DATABASE_PORT = 3333
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'


current_env = os.getenv('FLASK_ENV')
