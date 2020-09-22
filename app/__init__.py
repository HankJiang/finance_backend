from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery

from app import config

db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config.current_env == 'production':
        app.config.from_object(config.Production)
    else:
        app.config.from_object(config.Development)

    from app.controllers import auth
    from app.controllers import stock
    from app.controllers import test
    app.register_blueprint(auth.bp)
    app.register_blueprint(stock.bp)
    app.register_blueprint(test.bp)

    # cors
    app.url_map.strict_slashes = False
    CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})

    # db
    db.init_app(app)
    Migrate(app, db)

    return app


def create_celery(app):
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'], include=['app.tasks.stock_tasks'])
    celery.conf.update(app.config)

    return celery


app = create_app()
celery = create_celery(app)
