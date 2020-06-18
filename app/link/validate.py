from flask import request

from app.link.models import Link, Location
from app.ripple.models import Ripple

def getArgs():
    json = request.json
    if 'parent_id' not in json:
        return None

    location = None
    if 'start_location' in json:
        loc = json['start_location']
        location = Location(loc['lat'], loc['lon'])

    return json['parent_id'], json.get('user_id', None), location

def getRippleId():
    json = request.json
    if 'parent_id' not in json:
        return False
    parent_id = json['parent_id']
    parent = Link.queryById(parent_id)
    return str(parent['ripple_id'])

def validateNewLink(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        ripple_id = getRippleId()
        if ripple_id == None:
            return "Invalid Ripple Id", 422

        result = f(ripple_id, *args)
        return result
    return func
