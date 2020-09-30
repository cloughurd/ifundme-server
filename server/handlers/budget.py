from abc import ABC
from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase, respond, handle_key_error
from server.handlers.requests.budget import CreateBudgetRequest
from server.services.budget import BudgetService


class BudgetHandler(HandlerBase, ABC):
    def __init__(self, service: BudgetService):
        self.service = service

    @respond
    @handle_key_error
    def create(self, r: Request, **kwargs):
        group_name = kwargs['group_name']
        body = r.get_json()
        try:
            budget_request = CreateBudgetRequest(**body)
        except TypeError as e:
            raise InvalidRequestException('invalid create budget request body', e)
        total_percentage = sum([entry.percentage for entry in budget_request.categories])
        if total_percentage < 99 or total_percentage > 101:
            raise InvalidRequestException('budget entry percentages do not sum to 100%')
        budget_response = self.service.create(group_name, budget_request)
        return budget_response.to_response()
