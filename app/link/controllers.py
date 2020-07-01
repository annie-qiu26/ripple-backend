from flask import Blueprint, request

from app.link.models import Link
from app import db

from app.link.validate import validateNewLink
from app.link.descendents import increment_descendent_counts, increment_child_counts

blueprint = Blueprint('link', __name__)

"""
Request Body Parameters:
    parent_id: str, required
    user_id: str, optional
    start_location: 
        lat: float
        lon: float
Example curl request:
curl -X POST --data '{"parent_id":"___"}' --header "Content-Type: application/json" localhost:5000/api/link
"""
@blueprint.route('/api/link', methods=['POST'])
@validateNewLink
def create_link(ripple_id, parent_id, user_id, start_location):
    link = Link(ripple_id=ripple_id, parent_id=parent_id, user_id=user_id, start_location=start_location)
    increment_descendent_counts(parent_id)
    increment_child_counts(parent_id)
    link_id = link.save()
    return {"ripple_id": str(ripple_id), "link_id": str(link_id)}

"""
Request Query Parameters:
token: str
"""
@blueprint.route('/api/link/<link_id>', methods=['GET'])
def find_link(link_id):
    link = Link.queryById(link_id)
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
