from server.exceptions.server import InvalidRequestException
from server.utils.constants import RequestBodyKeys
from server.utils.validators import is_positive_number


class BudgetRequestEntry:
    def __init__(self, **kwargs):
        self.name = kwargs.pop(RequestBodyKeys.CATEGORY_NAME.value)
        self.percentage = kwargs.pop(RequestBodyKeys.PERCENTAGE.value)
        if not is_positive_number(self.percentage):
            raise InvalidRequestException('invalid category percentage value')
        self.builds = kwargs.pop(RequestBodyKeys.BUILDS.value)
        if not isinstance(self.builds, bool):
            raise InvalidRequestException('invalid category builds value')
        if kwargs:
            raise InvalidRequestException('unexpected values in create budget request body')


class CreateBudgetRequest:
    def __init__(self, **kwargs):
        self.projected_income = kwargs.pop(RequestBodyKeys.PROJECTED_INCOME.value)
        if not is_positive_number(self.projected_income):
            raise InvalidRequestException('invalid projected income value')
        categories = kwargs.pop(RequestBodyKeys.CATEGORIES.value)
        self.categories = [BudgetRequestEntry(**c) for c in categories]
        if kwargs:
            raise InvalidRequestException('unexpected values in create budget request body')
