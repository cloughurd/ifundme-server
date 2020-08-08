from server.models.budget import Category


class BudgetRequestEntry:
    def __init__(self, name: str, percentage: float, builds: bool):
        self.name = name
        self.percentage = percentage
        self.builds = builds


class CreateBudgetRequest:
    def __init__(self, projectedIncome: float, entries: list):
        self.projected_income = projectedIncome
        self.entries = [BudgetRequestEntry(**entry) for entry in entries]
