from flask import request

def getArgs():
    json = request.json
    if 'name' not in json:
        return None
    if 'url' not in json:
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