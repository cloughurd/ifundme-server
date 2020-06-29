from datetime import date

from server.exceptions.server import InvalidRequestException
from server.exceptions.storage import DuplicateResourceIdException
from server.models.user import User
from server.storage.user import UserStorage


class UserService:
    def __init__(self, storage: UserStorage):
        self.storage = storage

    def create(self, username: str):
        # TODO: Use passwords
        try:
            u = self.storage.create_user(username, 'password')
        except DuplicateResourceIdException as e:
            raise InvalidRequestException('username already exists', e)
        return FilteredUser(u)

    def update(self, username: str):
        u = self.storage.update_user(username)
        return FilteredUser(u)

    def list(self):
        users = self.storage.list_users()
        return [FilteredUser(u) for u in users]


class FilteredUser:
    def __init__(self, full_user: User):
        self.username = full_user.username
        self.date_created: date = full_user.date_created
        self.date_last_accessed: date = full_user.date_last_accessed

    def to_response(self):
        return {
            'username': self.username,
            'dateCreated': self.date_created.isoformat(),
            'dateLastAccessed': self.date_last_accessed.isoformat()
        }
