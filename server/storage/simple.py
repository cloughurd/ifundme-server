import os
import pickle
from datetime import date
import logging

from server.exceptions.storage import StorageAccessException, ResourceNotFoundException, DuplicateResourceIdException
from server.models.group import Group
from server.models.membership import Membership
from server.models.user import User
from server.storage.group import GroupStorage
from server.storage.membership import MembershipStorage
from server.storage.user import UserStorage
from server.utils.ids import IdGenerator


class SimpleStorage(UserStorage, MembershipStorage, GroupStorage):
    def __init__(self, filename=None):
        self.logger = logging.getLogger(__name__)
        if filename is None:
            self.filename = os.environ.get('IFM_STORAGE_FILE', 'simpleStorage.pickle')
        else:
            self.filename = filename
        if os.path.isfile(self.filename):
            try:
                self.data = pickle.load(open(self.filename, 'rb'))
            except Exception as e:
                raise StorageAccessException('simple storage', e)
        else:
            self.data = Data()

    def create_user(self, username: str, password_hash: str) -> User:
        if username in self.data.user:
            raise DuplicateResourceIdException(username, 'user')
        u = User(username, password_hash, date.today(), date.today())
        self.data.user[username] = u
        self.save()
        return u

    def update_user(self, username) -> User:
        if username not in self.data.user:
            raise ResourceNotFoundException(username, 'user')
        u = self.data.user[username]
        u.date_last_accessed = date.today()
        self.save()
        return u

    def list_users(self) -> list:
        return list(self.data.user.values())

    def create_group(self, group_name: str, group_pin: str) -> Group:
        if group_name in self.data.group:
            raise DuplicateResourceIdException(group_name, 'group')
        g = Group(group_name, group_pin, date.today())
        self.data.group[group_name] = g
        self.save()
        return g

    def create_membership(self, username: str, group_name: str, member_type: str) -> Membership:
        if username not in self.data.user:
            raise ResourceNotFoundException(username, 'user')
        if group_name not in self.data.group:
            raise ResourceNotFoundException(group_name, 'group')
        m = Membership(username, group_name, member_type, date.today(), IdGenerator.generate_membership_id())
        self.data.membership.append(m)
        self.save()
        return m

    def update_membership(self, membership_id: str, change_field: str, change_value: str) -> Membership:
        for m in self.data.membership:
            if m.membership_id == membership_id:
                if change_field == 'type':
                    m.member_type = change_value
                    self.save()
                    return m
        raise ResourceNotFoundException(membership_id, 'membership')

    def search_memberships(self, search_type: str, search_id: str) -> list:
        results = []
        for m in self.data.membership:
            if search_type == 'username':
                if m.username == search_id:
                    results.append(m)
            if search_type == 'group':
                if m.group_name == search_id:
                    results.append(m)
        return results

    def save(self):
        try:
            pickle.dump(self.data, open(self.filename, 'wb'))
        except Exception as e:
            self.logger.exception('Error pickling data')
            raise StorageAccessException('simple storage', e)


class Data:
    def __init__(self, user=None, membership=None, group=None):
        if group is None:
            group = {}
        if membership is None:
            membership = []
        if user is None:
            user = {}
        self.user = user
        self.membership = membership
        self.group = group
