from app.database import Model
from app import db

class User(Model):
    collection = db.users

    def __init__(self):
        self._id = None # str
        self.email = None # str
        
        self.ripple_to_link = {} # ripple_id: link_id
        self.link_child_index = {} # link_id: child index

    def get_link(self, ripple_id):
        return self.ripple_to_link.get(ripple_id, None)

    def set_ripple_link(self, ripple_id, link_id, index):
        self.ripple_to_link[ripple_id] = link_id
        self.link_child_index[link_id] = index
    
    def get_link_index(self, link_id):
        return self.link_child_index.get(link_id, 0)