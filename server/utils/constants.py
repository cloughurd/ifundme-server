from enum import Enum


class RequestBodyKeys(Enum):
    GROUP_NAME = 'groupName'
    USERNAME = 'username'
    MEMBER_TYPE = 'memberType'
    PROJECTED_INCOME = 'projectedIncome'
    CATEGORIES = 'categories'
    CATEGORY_ID = 'categoryId'
    CATEGORY_NAME = 'categoryName'
    PERCENTAGE = 'percentage'
    BUILDS = 'builds'
    TRANSACTION_TYPE = 'transactionType'
    TRANSACTION_DATE = 'transactionDate'
    AMOUNT = 'amount'
    DESCRIPTION = 'description'
    ACCOUNT = 'account'


class ResponseBodyKeys:
    result = 'result'
    username = 'username'
    users = 'users'


class TransactionType(Enum):
    EXPENSE = 'expense'
    INCOME = 'income'
    WITHDRAWAL = 'withdrawal'
    DEPOSIT = 'deposit'


class MemberType(Enum):
    LEADER = 'leader'
    MEMBER = 'member'
