from flask import Blueprint, request

blueprint = Blueprint('link_node', __name__)

# TODO: Delete example test function
@blueprint.route('/api/link_node/test', methods=['GET'])
def test():
    body = request.json
    return "<h1>Hello World!</h1>"

@blueprint.route('/api/link_node/create', methods=['POST'])
def create_link_node():
    pass

@blueprint.route('/api/link_node/<token>', methods=["GET"])
def get_link_node(token):
    pass

@blueprint.route('/api/link_node/child', methods=["PUT"])
def add_ripple_child_node():
    pass
