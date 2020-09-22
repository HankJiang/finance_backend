from functools import wraps
import logging
from datetime import datetime


def time_log(func):
    @wraps(func)
    def log(*args,**kwargs):
        logging.info("{} {}=========Start".format(datetime.now().strftime("%Y-%m-%d %H:%M"), func.__name__))
        result = func(*args,**kwargs)
        logging.info("{} {}=========End".format(datetime.now().strftime("%Y-%m-%d %H:%M"), func.__name__))
        return result
    return log