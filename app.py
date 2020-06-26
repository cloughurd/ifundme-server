from flask import Flask, jsonify
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
        unknown_error = ServerException(e)
        return build_response(unknown_error.to_response(), unknown_error.get_code())


@app.route('/health')
def health():
    factory.handlers.health.get()
    return build_response('all is well')


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)
