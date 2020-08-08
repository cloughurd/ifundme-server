from server.models.summary import FundSummary, GroupSummary


class SummaryService:
    def __init__(self, storage: BudgetStorage):
        pass

    def generate_summary(self, group_name: str) -> GroupSummary:

        fund_summaries = [
            FundSummary(132.34, 164.35, 62.17)
        ]
        group_summary = GroupSummary(888.88, 999.99, 312.54, fund_summaries)
        return group_summary
