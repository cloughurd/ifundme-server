from abc import ABC
from datetime import date
from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase
from server.handlers.requests.transaction import CreateTransactionRequest


class TransactionHandler(HandlerBase, ABC):
    def get(self, r: Request, **kwargs):
        pass

    def get_many(self, r: Request, **kwargs):
        pass

    def create(self, r: Request, **kwargs):
        body = r.get_json()
        transaction_request = CreateTransactionRequest(**body)
        if transaction_request.transaction_date > date.today():
            # TODO: is this desirable?
            raise InvalidRequestException('cannot create a request for a future date')
        # TODO: build and call transaction service

    def update(self, r: Request, **kwargs):
        pass

    def search(self, r: Request, **kwargs):
        pass
