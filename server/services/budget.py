from server.handlers.requests.budget import CreateBudgetRequest
from server.storage.interfaces.budget import BudgetStorage


class BudgetService:
    def __init__(self, storage: BudgetStorage):
        self.storage = storage

    def create(self, group_name: str, budget_request: CreateBudgetRequest):
        fund_count = 0
        category_count = 0
        self.storage.create_income(group_name, budget_request.projected_income)
        for entry in budget_request.categories:
            category = self.storage.create_budget_category(group_name, entry)
            category_count += 1
            if entry.builds:
                self.storage.create_fund(category.category_id)
                fund_count += 1
        response = CreateBudgetResponse(fund_count, category_count)
        return response


class CreateBudgetResponse:
    def __init__(self, funds_created, categories_created):
        self.funds_created = funds_created
        self.categories_created = categories_created

    def to_response(self):
        return {
            'fundsCreated': self.funds_created,
            'categoriesCreated': self.categories_created
        }
