from flask import Blueprint, request

blueprint = Blueprint('link', __name__)

# TODO: Delete example test function
@blueprint.route('/api/link/test', methods=['GET'])
def test():
    body = request.json
    return "<h1>Hello World!</h1>"

"""
Request Body Parameters:

"""
@blueprint.route('/api/link', methods=['POST'])
def create_link():
    pass

"""
Request Query Parameters:
token: str
"""
@blueprint.route('/api/link', methods=['GET'])
def find_link():
    pass

"""
Request Body Parameters:
total_views: int
total_unique_visitors: int
total_children: int 
total_descendants: int
total_depth: int 
total_raised: int 
total_miles: int
added_location: str
"""
@blueprint.route('/api/link', methods=["PUT"])
def update_link():
    pass
