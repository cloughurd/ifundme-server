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
