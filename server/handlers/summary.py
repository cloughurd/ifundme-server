from abc import ABC
from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase, respond, handle_key_error
from server.services.summary import SummaryService


class SummaryHandler(HandlerBase, ABC):
    def __init__(self, service: SummaryService):
        self.service = service

    @respond
    @handle_key_error
    def get(self, r: Request, **kwargs):
        group_name = kwargs['group_name']
        summary = self.service.generate_summary(group_name)
        return summary.to_response()
