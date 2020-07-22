from server.models.budget import BudgetEntry


class BudgetRequestEntry(BudgetEntry):
    def __init__(self, name: str, percentage: float, builds: bool):
        super().__init__(name, percentage)
        self.builds = builds


class CreateBudgetRequest:
    def __init__(self, projectedIncome: float, entries: list):
        self.projected_income = projectedIncome
        self.entries = [BudgetRequestEntry(**entry) for entry in entries]
