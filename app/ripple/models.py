from app.database import Model
from app import db

class Ripple(Model):
    collection = db.ripples

    def __init__(self, title=None, org_ids=[]):
        self._id = None # str, token that uniquely identiifes Ripple
        self.root_id = None # str, token that points to the root Node
        
        self.created_at = None # DateTime

        self.title = title
        self.organizations = org_ids # [str or organization ids]

    def dict(self):
        return self.__dict__