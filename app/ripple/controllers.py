from flask import Blueprint, request

blueprint = Blueprint('ripple', __name__)

# TODO: Delete example test function
@blueprint.route('/api/ripple/test', methods=['GET'])
def test():
    body = request.json
    return "<h1>Hello World!</h1>"

@blueprint.route('/api/ripple', methods=['POST'])
def create_ripple():
    pass

@blueprint.route('/api/ripple', methods=["GET"])
def find_ripple(token):
    pass

@blueprint.route('/api/ripple', methods=["PUT"])
def update_ripple():
    pass
