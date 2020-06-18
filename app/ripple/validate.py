from flask import request

from app.link.models import Location

def getArgs():
    json = request.json

    location = None
    if 'start_location' in json:
        loc = json['start_location']
        location = Location(loc['lat'], loc['lon'])

    return json.get('user_id', None), location

def validateNewRipple(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        result = f(*args)
        return result
    return func