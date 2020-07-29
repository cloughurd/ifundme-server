from flask import Request


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


def respond(func):
    def make_response(self: HandlerBase, r: Request, **kwargs):
        result = func(self, r, **kwargs)
        return {
            'result': result
        }
    return make_response
