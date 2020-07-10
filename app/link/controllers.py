from flask import Blueprint, request, make_response, abort

from app.link.models import Link
from app.ripple.models import Ripple
from app.user.controllers import user_from_cookie
from app import db

from app.link.validate import validateNewLink
from app.link.updates import increment_descendent_counts, increment_child_counts, update_depth

blueprint = Blueprint('link', __name__)

def create_link(ripple_id, parent_id, user_id, start_location):
    link = Link(ripple_id=ripple_id, parent_id=parent_id, user_id=user_id, start_location=start_location)
    increment_descendent_counts(parent_id)
    increment_child_counts(parent_id)
    update_depth(parent_id)
    link_id = link.save()
    return link_id

def find_ripple_link(link_id):
    link = Link.queryById(link_id)
    if link == None:
        return None, None

    ripple = Ripple.queryById(link.ripple_id)
    if ripple == None:
        return None, None

    return link, ripple

@blueprint.route('/api/ripple', methods=['OPTIONS'])
def options_route():
    resp = make_response({})
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp

@blueprint.route('/api/link/<link_id>', methods=['GET'])
def find_route(link_id):
    link, ripple = find_ripple_link(link_id)
    if link == None or ripple == None:
        abort(404)
    return {"link": link.dict(), "ripple": ripple.dict()}

@blueprint.route('/api/link/<link_id>', methods=['POST'])
def visit_route(link_id):
    # get old link and ripple info
    _, ripple = find_ripple_link(link_id)
    if ripple == None:
        abort(404)

    # get the user's link_id associated with thie ripple
    user = user_from_cookie(request)
    user_link_id = user.get_link(ripple._id)

    # if user does not have link with this ripple, make one
    if user_link_id == None:
        user_link_id = create_link(ripple._id, link_id, None, None)
        child_index = link.total_children + 1 # the total children + 1 == how many links were created before this
        user.set_ripple_link(ripple._id, user_link_id, child_index)
    uid = user.save()

    # get the link the user has associated with ripple
    link = Link.queryById(user_link_id)
    viewNo = user.get_link_index(user_link_id)
    resp = make_response({"link": link.dict(), "ripple": ripple.dict(), "view_no": str(viewNo)})

    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.set_cookie("uid", uid)

    return resp