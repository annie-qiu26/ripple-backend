from flask import request

from app.link.models import Location
from app.organization.models import Organization

def getArgs():
    json = request.json
    if type(json.get('organizations', None)) != list:
        return None

    location = None
    if 'start_location' in json:
        loc = json['start_location']
        location = Location(loc['lat'], loc['lon'])

    return json['organizations'], json.get('user_id', None), location

def checkOrganizations():
    json = request.json
    for org_id in json['organizations']:
        org = Organization.queryById(org_id)
        if not org:
            return False
    return True

def validateNewRipple(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        if not checkOrganizations():
            return "Invalid Organization Id", 422

        result = f(*args)
        return result
    return func