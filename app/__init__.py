from flask import Flask
from flask_cors import CORS
import config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if config.current_env == 'production':
        app.config.from_object(config.Production)
    else:
        app.config.from_object(config.Development)

    from app.controllers import auth
    from app.controllers import stock
    app.register_blueprint(auth.bp)
    app.register_blueprint(stock.bp)

    # cors
    app.url_map.strict_slashes = False
    CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})

    return app


app = create_app()
