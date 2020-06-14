from app.database import Model

class Link(Model):
    def __init__(self):
        self.id = None # str, token that uniquely identiifes Node
        self.parent_id = None # str, token that points to the parent Node
        self.ripple_id = None # str, token that points to Ripple this Node is in
        self.user_id = None # Optional

        self.created_at = None # DateTime

        self.total_views = None # int
        self.total_unique_visitors = None # int
        # ^ though how do we keep track of people visiting?
        # (Google Analytics does this somehow?)
        self.total_children = None # int 
        self.total_descendants = None # int
        self.total_depth = None # int
        self.total_raised = None # int
        self.total_miles = None # int
        
        self.start_location = None # str
        self.farthest_location = None # str
        self.last_location = None # str
