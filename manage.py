import click
import os
from peewee_migrate import Router
from app.db import db

router = Router(db)


@click.group()
def db():
    pass


@db.command()
@click.argument('migration_name')
def db_create(migration_name):
    router.create(migration_name)


@db.command()
def db_upgrade():
    last_migrate = os.listdir('./migrations')[-1][0:-3]
    router.run(last_migrate)


@db.command()
def db_downgrade():
    last_migrate = os.listdir('./migrations')[-1][0:-3]
    router.rollback(last_migrate)


commands = click.CommandCollection(sources=[db])

if __name__ == '__main__':
    commands()
