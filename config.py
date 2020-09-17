import os
from flask import Config


class Development(Config):
    DEBUG = True
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/finance'


class Production(Config):
    DEBUG = False
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = 'mysql'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@mysql/finance'


current_env = os.getenv('FLASK_ENV')
