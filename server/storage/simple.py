import os
import pickle
from datetime import date
import logging

from server.exceptions.storage import StorageAccessException, ResourceNotFoundException, DuplicateResourceIdException
from server.models.user import User
from server.storage.user import UserStorage


class SimpleStorage(UserStorage):
    def __init__(self, filename=None):
        self.logger = logging.getLogger(__name__)
        if filename is None:
            self.filename = os.environ.get('IFM_STORAGE_FILE', 'simpleStorage.pickle')
        if os.path.isfile(self.filename):
            try:
                self.user_data = pickle.load(open(self.filename, 'rb'))
            except Exception as e:
                raise StorageAccessException('simple storage', e)
        else:
            self.user_data = {}

    def create_user(self, username: str, password_hash: str) -> User:
        if username in self.user_data:
            raise DuplicateResourceIdException(username, 'user')
        u = User(username, password_hash, date.today(), date.today())
        self.user_data[username] = u
        self.save()
        return u

    def update_user(self, username):
        if username not in self.user_data:
            raise ResourceNotFoundException(username, 'user')
        u = self.user_data[username]
        u.date_last_accessed = date.today()
        self.save()
        return u

    def list_users(self) -> list:
        return list(self.user_data.values())

    def save(self):
        try:
            pickle.dump(self.user_data, open(self.filename, 'wb'))
        except Exception as e:
            self.logger.exception('Error pickling data')
            raise StorageAccessException('simple storage', e)
