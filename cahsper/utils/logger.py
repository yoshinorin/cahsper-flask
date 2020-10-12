from flask import Blueprint, Response, request
from functools import wraps
from cahsper import cahsper

def http_request_logging(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            cahsper.logger.info('%s - %s - %s - %s', request.remote_addr, request.method, request.url, request.query_string)
        except Exception as e:
            cahsper.logger.exception(e)
            pass
        return f(*args, **kwargs)
    return decorated_function
