import uuid


class IdGenerator:
    membership_prefix = 'MEM_'
    fund_prefix = 'FND_'
    category_prefix = 'CAT_'
    expense_prefix = 'EXP_'
    income_prefix = 'INC_'

    @staticmethod
    def generate_membership_id():
        return IdGenerator.membership_prefix + str(uuid.uuid4())

    @staticmethod
    def generate_fund_id():
        return IdGenerator.fund_prefix + str(uuid.uuid4())

    @staticmethod
    def generate_category_id():
        return IdGenerator.category_prefix + str(uuid.uuid4())

    @staticmethod
    def generate_expense_id():
        return IdGenerator.expense_prefix + str(uuid.uuid4())

    @staticmethod
    def generate_income_id():
        return IdGenerator.income_prefix + str(uuid.uuid4())
