# Import the database object from the main app module
from app import db
import re
from bson.objectid import ObjectId

class Model():
    """
    A wrapper for mongodb documents
    """
    def __init__(self):
        pass

    def dict(self):
        dic = {}
        dic.update(self.__dict__)
        return dic

    def save(self):
        if self.__class__.collection == None:
            raise Exception("No database collection specified")
        dic = self.dict()
        objId = dic['_id']
        del dic['_id']
        if objId == None:
            objId = str(self.__class__.collection.save(dic))
        else:
            self.__class__.collection.update_one({'_id': ObjectId(objId)}, {'$set': dic})

        self._id = objId
        return objId

    @classmethod
    def queryById(cls, id):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            dic = cls.collection.find_one({'_id': ObjectId(id)})
            dic['_id'] = id

            obj = cls()
            for k, v in dic.items():
                setattr(obj, k, v)
            return obj
        except Exception:
            return None

    @classmethod
    def queryAll(cls):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            documents = cls.collection.find({})
            res = []
            for doc in documents:
                doc['_id'] = str(doc['_id'])

                obj = cls()
                for k, v in doc.items():
                    setattr(obj, k, v)
                res.append(obj)
            return res
        except Exception:
            return None

    @classmethod
    def fuzzySearch(cls, attribute, query):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            escaped = re.sub(r'[-[\]{}()*+?.,\\^$|#\s]', "\\$&", query)
            regex = re.compile(escaped, flags=re.I)

            documents = cls.collection.find({ attribute: regex })
            results = []
            for i, doc in enumerate(documents):
                doc['_id'] = str(doc['_id'])
                results.append(doc)

            return results
        except Exception:
            return None

    @classmethod
    def incrementField(cls, id, field):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            dic = cls.collection.find_and_modify({'_id': ObjectId(id)}, {"$inc": { field: 1 }})
            dic['_id'] = id

            obj = cls()
            for k, v in dic.items():
                setattr(obj, k, v)
            return obj
        except Exception as e:
            print(e)
            return None

    @classmethod
    def setField(cls, id, field, value):
        if cls.collection == None:
            raise Exception("No database collection specified")
        try:
            dic = cls.collection.find_and_modify({'_id': ObjectId(id)}, {"$set": { field: value }})
            dic['_id'] = id

            obj = cls()
            for k, v in dic.items():
                setattr(obj, k, v)
            return obj
        except Exception as e:
            print(e)
            return None