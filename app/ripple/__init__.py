class Link:
    def __init__(self):
        self.id = None # String, token that uniquely identiifes Node
        self.parent_id = None # String, token that points to the parent Node
        self.user_id = None # Optional

        self.created_at = None # DateTime

        self.total_views = None # Int
        self.total_unique_visitors = None # Int
        # ^ though how do we keep track of people visiting?
        # (Google Analytics does this somehow?)
        self.total_children = None # Int 
        self.total_descendants = None # Int
        self.total_depth = None # Int
        self.total_raised = None # Int
        self.total_miles = None # Int
        
        self.start_location = None # String
        self.farthest_location = None # String

        self.organizations = [] # [String]
