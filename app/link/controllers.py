from flask import Blueprint, request

from app.link.models import Link
from app import db

from app.link.validate import validateRequestBody

blueprint = Blueprint('link', __name__)

# TODO: Delete example test function
@blueprint.route('/api/link/test', methods=['GET'])
def test():
    body = request.json
    return "<h1>Hello World!</h1>"

"""
Request Body Parameters:
    ripple_id: str, required
    parent_id: str, None if root
    user_id: str, optional
    start_location: 
        lat: float
        lon: float
"""
@blueprint.route('/api/link', methods=['POST'])
@validateRequestBody
def create_link(ripple_id, parent_id, user_id, start_location):
    json = request.json
    
    link = Link(ripple_id=ripple_id, parent_id=parent_id, user_id=user_id, start_location=start_location)
    link.save()
    return "Success"

"""
Request Query Parameters:
token: str
"""
@blueprint.route('/api/link/<link_id>', methods=['GET'])
def find_link(link_id):
    print(link_id)
    link = Link()
    link.save()
    link = Link.queryById(link_id)
    print(link)
    return link

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
