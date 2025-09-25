from functools import wraps
from flask import request,abort

SECRET_KEY = "1505"

def check_access_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.headers.get("api-access-key") != SECRET_KEY:
            abort(403)
        return f(*args,**kwargs)
    return decorated