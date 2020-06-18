from flask import Blueprint, request

from app.ripple.models import Ripple
from app.ripple.validate import validateNewRipple

from app.link.models import Link

blueprint = Blueprint('ripple', __name__)

"""
Request Body Parameters:
    user_id: str, optional
    start_location: optional
        lat: float
        lon: float
"""
@blueprint.route('/api/ripple', methods=['POST'])
@validateNewRipple
def create_ripple(user_id, start_location):
    ripple = Ripple()
    ripple_id = ripple.save()

    root_link = Link(ripple_id=ripple_id, user_id=user_id, start_location=start_location)
    link_id = root_link.save()

    ripple.root_id = link_id
    ripple.save()
    return {"ripple_id": str(ripple_id), "link_id": str(link_id)}

@blueprint.route('/api/ripple', methods=["GET"])
def find_ripple(token):
    pass

@blueprint.route('/api/ripple', methods=["PUT"])
def update_ripple():
    pass
