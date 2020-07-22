from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound
import logging

from server.exceptions.server import ServerException
from server.utils.factory import create_factory
from server.utils.logs import setup_logger

setup_logger()
logger = logging.getLogger(__name__)
app = Flask(__name__)
factory = create_factory()


def build_response(content, code=200):
    response = jsonify(content)
    response.status_code = code
    return response


@app.errorhandler(Exception)
def handle_error(e: Exception):
    if isinstance(e, ServerException):
        return build_response(e.to_response(), e.get_code())
    elif isinstance(e, NotImplementedError):
        return build_response({'errorMessage': 'Sorry, the request cannot be completed'}, 418)
    elif isinstance(e, NotFound):
        return e
    else:
        logger.error(e)
        unknown_error = ServerException(e)
        return build_response(unknown_error.to_response(), unknown_error.get_code())


@app.route('/health', methods=['GET'])
def get_health():
    result = factory.handlers.health.get()
    return build_response(result)


@app.route('/users', methods=['GET'])
def list_users():
    result = factory.handlers.user.list(request)
    return build_response(result)


@app.route('/users', methods=['POST'])
def create_user():
    result = factory.handlers.user.create(request)
    return build_response(result)


@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    result = factory.handlers.user.update(request, username=username)
    return build_response(result)


@app.route('/memberships', methods=['POST'])
def create_membership():
    result = factory.handlers.membership.create(request)
    return build_response(result)


@app.route('/memberships/search', methods=['POST'])
def search_memberships():
    result = factory.handlers.membership.search(request)
    return build_response(result)


@app.route('/memberships/<membership_id>', methods=['PUT'])
def update_membership(membership_id):
    result = factory.handlers.membership.update(request, membership_id=membership_id)
    return build_response(result)


@app.route('/groups', methods=['POST'])
def create_group():
    result = factory.handlers.group.create(request)
    return build_response(result)


@app.route('/groups/<group_name>/budget', methods=['POST'])
def create_budget(group_name: str):
    pass


@app.route('/groups/<group_name>/summary', methods=['GET'])
def get_summary(group_name: str):
    pass


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)
