from flask import request

from app.link.models import Link
from app.ripple.models import Ripple

from app.location.utils import extractLocation

def getArgs():
    json = request.json
    if type(json.get('parent_id', None)) != str:
        return None

    loc = json.get('start_location', None)
    location = extractLocation(loc)

    user_id = None
    if type(json.get('user_id', None)) == str:
        user_id = json['user_id']

    return json['parent_id'], user_id, location

def getRippleId(parent_id):
    parent = Link.queryById(parent_id)
    if parent == None or parent.ripple_id == None:
        return None
    return str(parent.ripple_id)

def validateNewLink(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        ripple_id = getRippleId(args[0])
        if ripple_id == None:
            return "Invalid Ripple Id", 422

        result = f(ripple_id, *args)
        return result
    return func
