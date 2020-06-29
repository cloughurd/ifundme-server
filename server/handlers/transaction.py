from flask import Request

from server.handlers.base import HandlerBase


class TransactionHandler(HandlerBase):
    def get(self, r: Request, **kwargs):
        pass

    def get_many(self, r: Request, **kwargs):
        pass

    def create(self, r: Request, **kwargs):
        pass

    def update(self, r: Request, **kwargs):
        pass

    def search(self, r: Request, **kwargs):
        pass
