from abc import ABC
from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase, respond
from server.services.summary import SummaryService


class SummaryHandler(HandlerBase, ABC):
    def __init__(self, service: SummaryService):
        self.service = service

    @respond
    def get(self, r: Request, **kwargs):
        try:
            group_name = kwargs.get("group_name")
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
        summary = self.service.generate_summary(group_name)
        return summary.to_response()
