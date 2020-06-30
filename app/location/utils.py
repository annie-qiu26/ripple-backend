def extractLocation(loc):
    location = None
    if type(loc) == dict:
        lat, lon = loc.get('lat', None), loc.get('lon', None)
        if type(lat) == float and type(lon) == float:
            location = Location(lat, lon)

    return location