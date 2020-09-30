import os
import pickle
from datetime import date
import logging

from server.exceptions.storage import StorageAccessException, ResourceNotFoundException, DuplicateResourceIdException
from server.handlers.requests.budget import BudgetRequestEntry
from server.models.budget import Fund, Category, Income
from server.models.group import Group
from server.models.membership import Membership
from server.models.user import User
from server.storage.interfaces.budget import BudgetStorage
from server.storage.interfaces.group import GroupStorage
from server.storage.interfaces.membership import MembershipStorage
from server.storage.interfaces.user import UserStorage
from server.utils.ids import IdGenerator


class SimpleStorage(UserStorage, MembershipStorage, GroupStorage, BudgetStorage):
    def __init__(self, filename=None):
        self.logger = logging.getLogger(__name__)
        if filename is None:
            self.filename = os.environ.get('IFM_STORAGE_FILE', 'simpleStorage.pickle')
        else:
            self.filename = filename
        if os.path.isfile(self.filename):
            try:
                self.data = pickle.load(open(self.filename, 'rb'))
            except Exception:
                # raise StorageAccessException('simple storage', e)
                self.data = Data()
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
                    m.MEMBER_TYPE = change_value
                    self.save()
                    return m
        raise ResourceNotFoundException(membership_id, 'membership')

    def search_memberships(self, search_type: str, search_id: str) -> list:
        results = []
        for m in self.data.membership:
            if search_type == 'username':
                if m.USERNAME == search_id:
                    results.append(m)
            if search_type == 'group':
                if m.GROUP_NAME == search_id:
                    results.append(m)
        return results

    def get_income(self, group_name: str) -> Income:
        if group_name in self.data.incomes:
            return self.data.incomes[group_name]
        raise ResourceNotFoundException(f'income for {group_name}', 'income')

    def list_budget_categories(self, group_name: str) -> list:
        group_categories = [x for x in self.data.categories if x.GROUP_NAME == group_name]
        return group_categories

    def create_income(self, group_name: str, projected_income: float) -> Income:
        income = Income(group_name, projected_income)
        self.data.incomes[group_name] = income
        return income

    def create_budget_category(self, group_name: str, entry: BudgetRequestEntry) -> Category:
        category = Category(entry.name, group_name, entry.percentage)
        self.data.categories.append(category)
        return category

    def create_fund(self, category_id: str, balance=0) -> Fund:
        fund = Fund(category_id, balance, date.today(), date.today())
        self.data.funds[category_id] = fund
        return fund

    def save(self):
        try:
            pickle.dump(self.data, open(self.filename, 'wb'))
        except Exception as e:
            self.logger.exception('Error pickling data')
            raise StorageAccessException('simple storage', e)


class Data:
    def __init__(self, user=None, membership=None, group=None, categories=None, funds=None, incomes=None):
        if group is None:
            group = {}
        if membership is None:
            membership = []
        if user is None:
            user = {}
        if categories is None:
            categories = []
        if funds is None:
            funds = {}
        if incomes is None:
            incomes = {}
        self.user = user
        self.membership = membership
        self.group = group
        self.categories = categories
        self.funds = funds
        self.incomes = incomes
