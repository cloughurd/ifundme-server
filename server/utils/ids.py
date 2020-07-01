import uuid


class IdGenerator:
    membership_prefix = 'M_'

    @staticmethod
    def generate_membership_id():
        return IdGenerator.membership_prefix + str(uuid.uuid4())
