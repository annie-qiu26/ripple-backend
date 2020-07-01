from flask import request

from app.organization.models import Organization
from app.location.utils import extractLocation

def getArgs():
    json = request.json
    if type(json.get('organizations', None)) != list:
        return None

    loc = json.get('start_location', None)
    location = extractLocation(loc)

    user_id = None
    if type(json.get('user_id', None)) == str:
        user_id = json['user_id']

    return json['organizations'], user_id, location

def checkOrganizations():
    json = request.json
    for org_id in json['organizations']:
        org = Organization.queryById(org_id)
        if org == None:
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