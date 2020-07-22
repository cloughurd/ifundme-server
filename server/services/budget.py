from server.handlers.requests.budget import CreateBudgetRequest


class BudgetService:
    def __init__(self):
        pass

    def create(self, budget_request: CreateBudgetRequest):
        response = CreateBudgetResponse(0)
        return response


class CreateBudgetResponse:
    def __init__(self, funds_created):
        self.funds_created = funds_created

    def to_response(self):
        return {
            'fundsCreated': self.funds_created
        }
