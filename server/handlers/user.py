from abc import ABC

from flask import Request

from server.handlers.base import HandlerBase, respond, handle_key_error
from server.exceptions.server import InvalidRequestException
from server.services.user import UserService


class UserHandler(HandlerBase, ABC):
    def __init__(self, service: UserService):
        self.service = service

    @respond
    @handle_key_error
    def create(self, r: Request, **kwargs):
        body = r.get_json()
        username = body['username']
        u = self.service.create(username)
        return u.to_response()

    @respond
    @handle_key_error
    def update(self, r: Request, **kwargs):
        username = kwargs['username']
        u = self.service.update(username)
        return u.to_response()

    @respond
    def list(self, r: Request, **kwargs):
        users = self.service.list()
        return {
            'users': [u.to_response() for u in users]
        }
