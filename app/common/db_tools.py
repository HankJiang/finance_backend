from copy import deepcopy
from functools import wraps
from app import app


def app_context(func):
    @wraps(func)
    def context(*args,**kwargs):
        with app.app_context():
            return func(*args,**kwargs)
    return context()


def get_or_create(session, model, query_args, attr_args, save=False):
    instance = session.query(model).filter_by(**query_args).first()
    if instance:
        return instance
    else:
        data = deepcopy(query_args)
        data.update(attr_args)

        instance = model(**data)
        session.add(instance)

        if save:
            session.commit()

        return instance
