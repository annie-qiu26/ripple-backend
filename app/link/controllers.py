from flask import Blueprint, request, make_response, abort

from app.link.models import Link
from app.ripple.models import Ripple
from app import db

from app.link.validate import validateNewLink
from app.link.updates import increment_descendent_counts, increment_child_counts, update_depth

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
    update_depth(parent_id)
    link_id = link.save()
    return {"ripple_id": str(ripple_id), "link_id": str(link_id)}

@blueprint.route('/api/link/<link_id>', methods=['POST'])
def find_link(link_id):
    link = Link.queryById(link_id)
    if link == None:
        abort(404);

    ripple = Ripple.queryById(link.ripple_id)
    if ripple == None:
        abort(404)

    resp = make_response({"link": link.__dict__, "ripple": ripple.__dict__})
    resp.headers['Access-Control-Allow-Credentials'] = 'true'

    if request.cookies.get(link_id) == None:
        # increment views
        link.view()
        # set cookie
        resp.set_cookie(link_id, "1")

    return resp
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
    return ""
