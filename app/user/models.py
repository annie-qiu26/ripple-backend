from app.database import Model

class User(Model):
    def __init__(self):
        self.user_id = None # str
        self.email = None # str
        self.location = None # Optional, str

        self.created_at = None # DateTime
        
        self.links = None # [link_id]
        self.ripples = None # [ripple_id]

        self.total_unique_visitors = None # int
        # ^ though how do we keep track of people visiting?
        # (Google Analytics does this somehow?)
        self.total_children = None # int 
        self.total_descendants = None # int
        self.total_depth = None # int
        self.total_raised = None # int
        self.total_miles = None # int
