from flask import Blueprint, request

blueprint = Blueprint('user', __name__)

# TODO: Delete example test function
@blueprint.route('/api/user/test', methods=['GET'])
def test():
    body = request.json
    return "<h1>Hello World!</h1>"

@blueprint.route('/api/user', methods=['POST'])
def create_user():
    pass

@blueprint.route('/api/user', methods=["GET"])
def find_user(token):
    pass

@blueprint.route('/api/user', methods=["PUT"])
def update_user():
    pass
