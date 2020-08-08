from datetime import date


class Transaction:
    def __init__(self, transaction_date: date, amount: float, account: str, description: str, category_id: str, transaction_id=None):
        self.transaction_date = transaction_date
        self.amount = amount
        self.account = account
        self.description = description
