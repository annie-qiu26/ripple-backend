from flask import request

from app.link.models import Location
from app.ripple.models import Ripple

def getArgs():
    json = request.json
    if 'ripple_id' not in json:
        return None

    location = None
    if 'start_location' in json:
        loc = json['start_location']
        location = Location(loc['lat'], loc['lon'])

    return json['ripple_id'], json.get('parent_id', None), json.get('user_id', None), location

def validateRippleId():
    json = request.json
    if 'ripple_id' not in json:
        return False
    ripple_id = json['ripple_id']
    return Ripple.queryById(ripple_id)

def validateRequestBody(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        if not validateRippleId():
            return "Invalid Ripple Id", 422

        result = f(*args)
        return result
    return func
