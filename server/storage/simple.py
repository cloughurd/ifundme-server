import os
import json
from datetime import date

from server.exceptions.storage import StorageAccessException, ResourceNotFoundException, DuplicateResourceIdException
from server.models.user import User
from server.storage.user import UserStorage


class SimpleStorage(UserStorage):
    def __init__(self):
        self.filename = os.environ.get('IFM_STORAGE_FILE', 'simpleStorage.json')
        if os.path.isfile(self.filename):
            try:
                self.data = json.load(open(self.filename, 'r'))
            except Exception as e:
                raise StorageAccessException('simple storage', e)
        else:
            self.data = {}

    def create(self, username: str, password_hash: str) -> User:
        if username in self.data:
            raise DuplicateResourceIdException(username, 'user')
        u = User(username, password_hash, date.today(), date.today())
        self.data[username] = u
        try:
            json.dump(self.data, open(self.filename, 'w+'))
        except Exception as e:
            raise StorageAccessException('simple storage', e)
        return u

    def update(self, username):
        if username not in self.data:
            raise ResourceNotFoundException(username, 'user')
        u = self.data[username]
        u.date_last_accessed = date.today()
        return u

    def list(self) -> list:
        return list(self.data.values())
