from abc import ABC

from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase, respond, handle_key_error
from server.services.group import GroupService


class GroupHandler(HandlerBase, ABC):
    def __init__(self, service: GroupService):
        self.service = service

    @respond
    @handle_key_error
    def create(self, r: Request, **kwargs):
        body = r.get_json()
        group_name = body['groupName']
        group = self.service.create(group_name)
        return group.to_response()
