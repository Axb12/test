from functools import wraps

from flask import request

def query_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        query = request.get_json().get("query")
        if query is None:
            return "Error: query is required", 400
        return func(query=query, *args, **kwargs)
    return wrapper
