class Transaction:
    def __init__(self, transaction_date, amount, account, description):
        self.transaction_date = transaction_date
        self.amount = amount
        self.account = account
        self.description = description
