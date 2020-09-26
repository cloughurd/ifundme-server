from server.storage.interfaces.summary import SummaryStorage


class FundSummary:
    def __init__(self, name: str, earned: float, projected: float, spent: float, balance=None):
        self.name = name
        self.earned = earned
        self.projected = projected
        self.spent = spent
        self.balance = balance

    def to_response(self):
        response = {
            'name': self.name,
            "earned": self.earned,
            "projected": self.projected,
            "spent": self.spent
        }
        if self.balance is not None:
            response['balance'] = self.balance


class GroupSummary(FundSummary):
    def __init__(self, earned_income: float, projected_income: float, income_spent: float, fund_summaries: list):
        super().__init__(earned_income, projected_income, income_spent)
        self.fund_summaries = fund_summaries

    def to_response(self):
        return {
            "earnedIncome": self.earned,
            "projectedIncome": self.projected,
            "incomeSpent": self.spent,
            "fundSummaries": [s.to_response() for s in self.fund_summaries]
        }


class SummaryService:
    def __init__(self, storage: SummaryStorage):
        self.storage = storage

    def generate_summary(self, group_name: str) -> GroupSummary:

        fund_summaries = {}
        income = self.storage.get_income(group_name)
        summed_income = self.storage.sum_income_transactions(group_name)
        categories = self.storage.list_budget_categories(group_name)
        funds = self.storage.list_funds(group_name)
        total_spent = 0

        for c in categories:
            category_spent = self.storage.sum_category_transactions(c.category_id)
            total_spent += category_spent
            category_projected = income.amount * c.percentage
            category_earned = summed_income * c.percentage
            fund_summaries[c.category_id] = FundSummary(
                c.category_name, category_earned, category_projected, category_spent)

        for f in funds:
            fund_summary = fund_summaries[f.category_id]
            fund_summary.balance = f.balance

        group_summary = GroupSummary(summed_income, income.amount, total_spent, list(fund_summaries.items()))
        return group_summary
