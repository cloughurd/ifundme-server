from datetime import date

from server.exceptions.server import InvalidRequestException
from server.exceptions.storage import DuplicateResourceIdException
from server.models.group import Group
from server.storage.group import GroupStorage


class GroupService:
    def __init__(self, storage: GroupStorage):
        self.storage = storage

    def create(self, group_name: str):
        # TODO: use group PINs
        try:
            g = self.storage.create_group(group_name, 'pin')
        except DuplicateResourceIdException as e:
            raise InvalidRequestException('group name already exists', e)
        return FilteredGroup(g)


class FilteredGroup:
    def __init__(self, full_group: Group):
        self.group_name = full_group.group_name
        self.date_created: date = full_group.date_created

    def to_response(self):
        return {
            'groupName': self.group_name,
            'dateCreated': self.date_created.isoformat()
        }
