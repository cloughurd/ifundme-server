from typing import List

from server.models.budget import Income, Fund, Category
from server.models.transaction import Transaction
from server.storage.budget import BudgetStorage


class SummaryStorage:
    def __init__(self, budget_storage: BudgetStorage, transaction_storage=None):
        self.budget_storage = budget_storage
        self.transaction_storage = transaction_storage

    def get_income(self, group_name: str) -> Income:
        return self.budget_storage.get_income(group_name)

    def sum_income_transactions(self, group_name: str) -> float:
        raise NotImplementedError

    def list_budget_categories(self, group_name: str) -> List[Category]:
        return self.budget_storage.list_budget_categories(group_name)

    def list_funds(self, group_name: str) -> List[Fund]:
        raise NotImplementedError

    def sum_category_transactions(self, category_id: str) -> float:
        raise NotImplementedError

    def list_category_transactions(self, category_id: str) -> List[Transaction]:
        raise NotImplementedError
