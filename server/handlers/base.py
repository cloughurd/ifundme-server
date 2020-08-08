from flask import Request, request

from server.exceptions.server import InvalidRequestException


class HandlerBase:
    def get(self, r: Request, **kwargs):
        raise NotImplementedError

    def list(self, r: Request, **kwargs):
        raise NotImplementedError

    def create(self, r: Request, **kwargs):
        raise NotImplementedError

    def update(self, r: Request, **kwargs):
        raise NotImplementedError

    def search(self, r: Request, **kwargs):
        raise NotImplementedError


def handle_key_error(func):
    def catch_key_error(self: HandlerBase, r: request, **kwargs):
        try:
            result = func(self, r, **kwargs)
            return result
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
    return catch_key_error


def respond(func):
    def make_response(self: HandlerBase, r: Request, **kwargs):
        result = func(self, r, **kwargs)
        return {
            'result': result
        }
    return make_response
