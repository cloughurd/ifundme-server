from server.models.budget import Income
from server.storage.budget import BudgetStorage


class SummaryStorage:
    def __init__(self, budget_storage: BudgetStorage, transaction_storage=None):
        self.budget_storage = budget_storage
        self.transaction_storage = transaction_storage

    def get_income(self, group_name: str) -> Income:
        return self.budget_storage.get_income(group_name)

    def sum_income_transaction(self, group_name: str) -> float:
        raise NotImplementedError

    def list_budget_categories(self, group_name: str) -> list:
        return self.budget_storage.list_budget_categories(group_name)

    def sum_category_transactions(self, category_id: str) -> float:
        raise NotImplementedError

    def list_category_transactions(self, category_id: str) -> list:
        raise NotImplementedError
