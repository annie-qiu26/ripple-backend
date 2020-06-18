# Import the database object from the main app module
from app import db
from bson.objectid import ObjectId

class Model():
    """
    A wrapper for mongodb documents
    """
    def __init__(self):
        pass

    def dict(self):
        return {}

    def save(self):
        if self.__class__.collection == None:
            raise Exception("No database collection specified")
        dic = self.dict()
        del dic['_id']
        self.__class__.collection.save(dic)

    @classmethod
    def queryById(cls, id):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            dic = cls.collection.find_one({'_id': ObjectId(id)})
            if dic == None:
                return {}
            dic['_id'] = id
            return dic
        except Exception:
            return {}
