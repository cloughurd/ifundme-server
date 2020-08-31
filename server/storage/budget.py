from server.handlers.requests.budget import BudgetRequestEntry
from server.models.budget import Income, Category, Fund


class BudgetStorage:
    def get_income(self, group_name: str) -> Income:
        raise NotImplementedError

    def list_budget_categories(self, group_name: str) -> list:
        raise NotImplementedError

    def list_funds(self, group_name: str) -> list:
        raise NotImplementedError

    def create_income(self, group_name: str, projected_income: float) -> Income:
        raise NotImplementedError

    def create_budget_category(self, group_name: str, entry: BudgetRequestEntry) -> Category:
        raise NotImplementedError

    def create_fund(self, category_id: str, balance=0) -> Fund:
        raise NotImplementedError
