class LinkNode:
    def __init__(self):
        self.token = None
        self.email = None
        
        self.start_location = None
        self.locations = []
        self.charities = []

        self.depth_total = 0
        self.parent = 0
        self.children = []

        self.total_views = 0
        self.total_raised = 0
        self.total_nodes = 0
