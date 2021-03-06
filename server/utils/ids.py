import uuid


class IdGenerator:
    membership_prefix = 'MEM'
    fund_prefix = 'FND'
    category_prefix = 'CAT'
    expense_prefix = 'EXP'
    income_prefix = 'INC'
    transaction_prefix = 'TRN'

    @staticmethod
    def generate_membership_id():
        return IdGenerator._generate_id(IdGenerator.membership_prefix)

    @staticmethod
    def generate_fund_id():
        return IdGenerator._generate_id(IdGenerator.fund_prefix)

    @staticmethod
    def generate_category_id():
        return IdGenerator._generate_id(IdGenerator.category_prefix)

    @staticmethod
    def generate_expense_id():
        return IdGenerator._generate_id(IdGenerator.expense_prefix)

    @staticmethod
    def generate_income_id():
        return IdGenerator._generate_id(IdGenerator.income_prefix)

    @staticmethod
    def generate_transaction_id():
        return IdGenerator._generate_id(IdGenerator.transaction_prefix)

    '''
    Private method that forms IDs with specified prefix, one _,
    and then a random, unique id like abcdabcd-abcd-abcd-abcd-abcdabcdabcd
    '''
    @staticmethod
    def _generate_id(prefix: str):
        return f'{prefix}_{str(uuid.uuid4())}'
