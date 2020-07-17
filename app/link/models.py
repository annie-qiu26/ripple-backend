from datetime import datetime

from app.database import Model
from app import db
from app.location.models import Location

from bson.objectid import ObjectId

class Link(Model):
    collection = db.links

    def __init__(self, parent_id=None, ripple_id=None, user_id=None, start_location=None, child_index=1):
        super().__init__()

        self._id = None # str, token that uniquely identiifes Node
        self.parent_id = parent_id # str, token that points to the parent Node
        self.ripple_id = ripple_id # str, token that points to Ripple this Node is in
        self.user_id = user_id # Optional

        self.created_at = datetime.now() # DateTime

        self.total_views = 0 # int

        self.child_index = child_index # int
        self.total_children = 0 # int 
        self.total_descendants = 0 # int
        self.total_depth = 0 # int
        self.total_raised = 0 # int
        self.total_miles = 0 # int
        
        self.start_location = start_location # str
        self.farthest_location = None # str
        self.last_location = start_location # str

    def dict(self):
        dic = {}
        dic.update(self.__dict__)
        if self.start_location != None:
            dic['start_location'] = self.start_location.__dict__
        if self.farthest_location != None:
            dic['farthest_location'] = self.farthest_location.__dict__
        if self.last_location != None:
            dic['last_location'] = self.last_location.__dict__
        return dic

    @staticmethod
    def incrementField(id, field):
        try:
            dic = Link.collection.find_and_modify({'_id': ObjectId(id)}, {"$inc": { field: 1 }})
            dic['_id'] = id

            obj = Link()
            for k, v in dic.items():
                setattr(obj, k, v)
            return obj
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def setField(id, field, value):
        try:
            dic = Link.collection.find_and_modify({'_id': ObjectId(id)}, {"$set": { field: value }})
            dic['_id'] = id

            obj = Link()
            for k, v in dic.items():
                setattr(obj, k, v)
            return obj
        except Exception as e:
            print(e)
            return None