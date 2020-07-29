from abc import ABC

from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase
from server.services.group import GroupService


class GroupHandler(HandlerBase, ABC):
    def __init__(self, service: GroupService):
        self.service = service

    def create(self, r: Request, **kwargs):
        body = r.get_json()
        try:
            group_name = body['groupName']
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
        group = self.service.create(group_name)
        return group.to_response()
