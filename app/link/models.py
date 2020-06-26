from datetime import datetime

from app.database import Model
from app import db
from app.location.models import Location

class Link(Model):
    collection = db.links

    def __init__(self, parent_id=None, ripple_id=None, user_id=None, start_location=None):
        super().__init__()

        self._id = None # str, token that uniquely identiifes Node
        self.parent_id = parent_id # str, token that points to the parent Node
        self.ripple_id = ripple_id # str, token that points to Ripple this Node is in
        self.user_id = user_id # Optional

        self.created_at = datetime.now() # DateTime

        self.total_views = 0 # int
        self.total_unique_visitors = 0 # int
        # ^ though how do we keep track of people visiting?
        # (Google Analytics does this somehow?)
        self.total_children = 0 # int 
        self.total_descendants = 0 # int
        self.total_depth = 0 # int
        self.total_raised = 0 # int
        self.total_miles = 0 # int
        
        self.start_location = start_location # str
        self.farthest_location = None # str
        self.last_location = start_location # str

    def dict(self):
        dic = self.__dict__
        if self.start_location != None:
            dic['start_location'] = self.start_location.__dict__
        if self.farthest_location != None:
            dic['farthest_location'] = self.farthest_location.__dict__
        if self.last_location != None:
            dic['last_location'] = self.last_location.__dict__
        return dic

