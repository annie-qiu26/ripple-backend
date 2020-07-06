from flask import Blueprint, request

from app.ripple.models import Ripple
from app.link.models import Link
from app.ripple.validate import validateNewRipple


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
    ripple = Ripple(title, org_ids)
    ripple_id = ripple.save()

    root_link = Link(ripple_id=ripple_id, user_id=user_id, start_location=start_location)
    link_id = root_link.save()

    ripple.root_id = link_id
    ripple.save()
    return {"ripple_id": str(ripple_id), "link_id": str(link_id)}

@blueprint.route('/api/ripple/<rid>', methods=["GET"])
def find_ripple(rid):
    ripple = Ripple.queryById(rid)
    return ripple.__dict__

"""
"""
@blueprint.route('/api/ripple/list', methods=["GET"])
def list_ripples():
    allRipples = Ripple.queryAll()
    res = [{'_id': ripple._id, 'title': ripple.title} for ripple in allRipples]
    return {'res': res}
