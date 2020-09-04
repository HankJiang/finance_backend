from peewee import MySQLDatabase
import config


def get_db():
    config_class = config.Production if config.current_env == 'production' else config.Development
    database = MySQLDatabase(
        config_class.MYSQL_DATABASE_NAME,
        host=config_class.MYSQL_DATABASE_HOST,
        port=config_class.MYSQL_DATABASE_PORT,
        user=config_class.MYSQL_DATABASE_USER,
        passwd=config_class.MYSQL_DATABASE_PASSWORD
    )

    return database


db = get_db()
