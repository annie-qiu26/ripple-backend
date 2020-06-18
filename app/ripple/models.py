from app.database import Model
from app import db

class Ripple(Model):
    collection = db.ripples

    def __init__(self):
        self._id = None # str, token that uniquely identiifes Ripple
        self.root_id = None # str, token that points to the root Node
        
        self.created_at = None # DateTime

        self.organizations = [] # [str]

    def dict(self):
        return self.__dict__