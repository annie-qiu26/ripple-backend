from flask import Blueprint, request, abort

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

"""
Request Body Parameters:
    query: str, required
"""
@blueprint.route('/api/organization/search', methods=['POST'])
def search_route():
    json = request.json
    query = json.get('query', None)
    if type(query) != str:
        abort(422)

    orgs = Organization.fuzzySearch(query)
    return { "results": orgs }

@blueprint.route('/api/organization/<org_id>', methods=["GET"])
def find_organization(org_id):
    org = Organization.queryById(org_id)
    if org == None:
        abort(404);
    return org.__dict__

# list all organizations
@blueprint.route('/api/organization/list', methods=["GET"])
def list_organizations():
    allOrgs = Organization.queryAll()
    res = [{'_id': org._id, 'name': org.name} for org in allOrgs]
    return {'organizations': res}
