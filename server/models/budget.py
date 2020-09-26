from server.utils.ids import IdGenerator


class Category:
    def __init__(self, category_name: str, group_name: str, percentage: float,
                 date_created=None, date_updated=None, category_id=None):
        self.category_name = category_name
        self.group_name = group_name
        self.percentage = percentage
        self.date_created = date_created
        self.date_updated = date_updated
        if category_id is None:
            category_id = IdGenerator.generate_category_id()
        self.category_id = category_id


class Fund:
    def __init__(self, category_id: str, balance: float,
                 date_created=None, date_updated=None, fund_id=None):
        self.category_id = category_id
        self.balance = balance
        self.date_created = date_created
        self.date_updated = date_updated
        if fund_id is None:
            fund_id = IdGenerator.generate_fund_id()
        self.fund_id = fund_id


class Income:
    def __init__(self, group_name: str, amount: float,
                 date_created=None, date_updated=None, income_id=None):
        self.group_name = group_name
        self.amount = amount
        self.date_created = date_created
        self.date_updated = date_updated
        if income_id is None:
            income_id = IdGenerator.generate_income_id()
        self.income_id = income_id
