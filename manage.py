import click
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
@click.argument('migration_name')
def db_upgrade(migration_name):
    router.run(migration_name)


@db.command()
@click.argument('migration_name')
def db_downgrade(migration_name):
    router.rollback(migration_name)


commands = click.CommandCollection(sources=[db])

if __name__ == '__main__':
    commands()
