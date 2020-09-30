from datetime import date

from server.utils.constants import TransactionType
from server.utils.ids import IdGenerator


class Transaction:
    def __init__(self, transaction_date: date, amount: float, account: str, description: str,
                 category_id: str, transaction_type: TransactionType, transaction_id=None):
        self.transaction_date = transaction_date
        self.amount = amount
        self.account = account
        self.description = description
        self.category_id = category_id
        self.transaction_type = transaction_type
        if transaction_id is None:
            transaction_id = IdGenerator.generate_transaction_id()
        self.transaction_id = transaction_id
