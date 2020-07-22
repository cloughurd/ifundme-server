class FundSummary:
    def __init__(self, earned: float, projected: float, spent: float):
        self.earned = earned
        self.projected = projected
        self.spent = spent

    def to_response(self):
        return {
            "earned": self.earned,
            "projected": self.projected,
            "spent": self.spent
        }


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
