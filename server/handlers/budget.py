from abc import ABC

from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase
from server.handlers.requests.budget import CreateBudgetRequest


class BudgetHandler(HandlerBase, ABC):
    def __init__(self):
        pass

    def create(self, r: Request, **kwargs):
        body = r.get_json()
        try:
            budget_request = CreateBudgetRequest(**body)
        except TypeError as e:
            raise InvalidRequestException('invalid create budget request body', e)
        total_percentage = sum([entry.percentage for entry in budget_request.entries])
        if total_percentage < 99 or total_percentage > 101:
            raise InvalidRequestException('budget entry percentages do not sum to 100%')
