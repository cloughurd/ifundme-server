from server.exceptions.server import InvalidRequestException
from server.utils.constants import RequestBodyKeys, MemberType


class CreateMembershipRequest:
    def __init__(self, **kwargs):
        self.username = kwargs.pop(RequestBodyKeys.USERNAME.value)
        self.group_name = kwargs.pop(RequestBodyKeys.GROUP_NAME.value)
        try:
            self.member_type = MemberType(kwargs.pop(RequestBodyKeys.MEMBER_TYPE.value))
        except ValueError as e:
            raise InvalidRequestException('invalid member type', e)
        if kwargs:
            raise InvalidRequestException('unexpected values in create membership request body')
