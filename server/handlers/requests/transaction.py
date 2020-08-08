from datetime import date


class CreateTransactionRequest:
    def __init__(self, transactionDate: str, amount: float, categoryId: str, description: str, account: str):
        self.transaction_date = date.fromisoformat(transactionDate)
        self.amount = amount
        self.category_id = categoryId
        self.description = description
        self.account = account
