from datetime import date

from server.exceptions.server import InvalidRequestException
from server.utils.constants import TransactionType, RequestBodyKeys


class CreateTransactionRequest:
    def __init__(self, **kwargs):
        try:
            self.transaction_date = date.fromisoformat(kwargs.pop(RequestBodyKeys.TRANSACTION_DATE.value))
        except ValueError as e:
            raise InvalidRequestException('invalid date format', e)
        self.amount = kwargs.pop(RequestBodyKeys.AMOUNT.value)
        self.category_id = kwargs.pop(RequestBodyKeys.CATEGORY_ID.value)
        self.description = kwargs.pop(RequestBodyKeys.DESCRIPTION.value)
        self.account = kwargs.pop(RequestBodyKeys.ACCOUNT.value)
        try:
            self.transaction_type = TransactionType(kwargs.pop(RequestBodyKeys.TRANSACTION_TYPE.value))
        except ValueError as e:
            raise InvalidRequestException('invalid transaction type', e)
        if kwargs:
            raise InvalidRequestException('unexpected values in create transaction request body')
