from copy import deepcopy


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
