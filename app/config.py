import os
from flask import Config
from celery.schedules import crontab


schedules = {
    'load_stock': {
        'task': 'load_stock',
        "schedule": crontab(minute='15', hour='09', day_of_week='mon-fri')  # 工作日9:30
    },
    'load_stock_history': {
        'task': 'load_stock_history',
        "schedule": crontab(minute='30', hour='15', day_of_week='mon-fri')  # 工作日15:30
    }
}


class Development(Config):
    DEBUG = True
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/finance?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # celery-redis
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_IMPORTS = ["app.tasks"]
    CELERYBEAT_SCHEDULE = schedules


class Production(Config):
    DEBUG = False
    # mysql
    MYSQL_DATABASE_NAME = 'finance'
    MYSQL_DATABASE_HOST = 'mysql'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '123456'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@mysql/finance?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # celery-redis
    CELERY_BROKER_URL = 'redis://redis/0'
    CELERY_RESULT_BACKEND = 'redis://redis/0'
    CELERYBEAT_SCHEDULE = schedules
    CELERY_IMPORTS = ["app.tasks"]


current_env = os.getenv('FLASK_ENV')
