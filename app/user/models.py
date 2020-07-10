from app.database import Model
from app import db

class User(Model):
    collection = db.users

    def __init__(self):
        self._id = None # str
        self.email = None # str
        
        self.ripple_to_link = {} # ripple_id: link_id

    def get_link(self, ripple_id):
        return self.ripple_to_link.get(ripple_id, None)

    def set_ripple_link(self, ripple_id, link_id):
        self.ripple_to_link[ripple_id] = link_id
