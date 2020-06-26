from flask import request

def getArgs():
    json = request.json
    if type(json.get('name', None)) != str:
        return None
    if type(json.get('url', None)) != str:
        return None

    return json['name'], json['url'], json.get('category', None)

def validateNewOrganization(f):
    def func(*args, **kwargs):
        args = getArgs()
        if args == None:
            return "Invalid Request", 422

        result = f(*args)
        return result
    return func