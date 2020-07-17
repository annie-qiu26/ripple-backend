from datetime import datetime

from app.database import Model
from app import db

class Ripple(Model):
    collection = db.ripples

    def __init__(self, title=None, org_ids=[], start_location=None):
        self._id = None # str, token that uniquely identiifes Ripple
        self.root_id = None # str, token that points to the root Node
        
        self.created_at = datetime.now() # DateTime

        self.title = title
        self.organizations = org_ids # [str or organization ids]
        
        self.total_links = 1 # int 
        self.total_depth = 1 # int
        self.total_raised = 0 # int
        self.total_miles = 0 # int
        
        self.start_location = start_location # str
        self.farthest_location = None # str
