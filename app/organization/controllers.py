from flask import Blueprint, request

from app.organization.models import Organization
from app.organization.validate import validateNewOrganization

blueprint = Blueprint('organization', __name__)

"""
Request Body Parameters:
    name: str, required
    url: str, required
    category: str, optional
"""
@blueprint.route('/api/organization', methods=['POST'])
@validateNewOrganization
def create_organization(name, url, category):
    org = Organization(name, url, category=category)
    org.save()
    return "Success"

@blueprint.route('/api/organization/<org_id>', methods=["GET"])
def find_organization(org_id):
    org = Organization.queryById(org_id)
    return org.__dict__

@blueprint.route('/api/organization', methods=["PUT"])
def update_organization():
    pass
