from flask import Blueprint, request, make_response, abort

from app.ripple.models import Ripple
from app.link.models import Link
from app.ripple.validate import validateNewRipple
from app.user.controllers import user_from_cookie


blueprint = Blueprint('ripple', __name__)

"""
Request Body Parameters:
    title: str, required
    user_id: str, optional
    start_location: optional
        lat: float
        lon: float
    organizations: [org_ids], required
Example curl request:
curl -X POST --data '{"organizations": []}' --header "Content-Type: application/json" localhost:5000/api/ripple
"""
@blueprint.route('/api/ripple', methods=['POST'])
@validateNewRipple
def create_ripple(title, org_ids, user_id, start_location):
    ripple = Ripple(title=title, org_ids=org_ids, start_location=start_location)
    ripple_id = ripple.save()

    root_link = Link(ripple_id=ripple_id, user_id=user_id, start_location=start_location)
    link_id = root_link.save()

    ripple.root_id = link_id
    ripple.save()

    user = user_from_cookie(request)
    user.set_ripple_link(ripple_id, link_id)
    uid = user.save()

    resp = make_response({"ripple_id": ripple_id, "link_id": link_id})

    resp.set_cookie("uid", uid)

    return resp

@blueprint.route('/api/ripple/<rid>', methods=["GET"])
def find_ripple(rid):
    ripple = Ripple.queryById(rid)
    if ripple == None:
        abort(404)
    return ripple.__dict__

"""
"""
@blueprint.route('/api/ripple/list', methods=["GET"])
def list_ripples():
    allRipples = Ripple.queryAll()
    res = [{'_id': ripple._id, 'root_id': ripple.root_id, 'title': ripple.title} for ripple in allRipples]
    return {'ripples': res}


"""
Request Body Parameters:
    query: str, required
"""
@blueprint.route('/api/ripple/search', methods=['POST'])
def search_route():
    json = request.json
    query = json.get('query', None)
    if type(query) != str:
        abort(422)

    ripples = Ripple.fuzzySearch('title', query)
    print(query)
    return {"ripples": ripples}
