import os

from server.handlers.budget import BudgetHandler
from server.handlers.group import GroupHandler
from server.handlers.health import HealthHandler
from server.handlers.membership import MembershipHandler
from server.handlers.summary import SummaryHandler
from server.handlers.user import UserHandler
from server.services.budget import BudgetService
from server.services.group import GroupService
from server.services.membership import MembershipService
from server.services.summary import SummaryService
from server.services.user import UserService
from server.storage.simple import SimpleStorage


class StorageFactory:
    def __init__(self):
        self.storage = SimpleStorage()
        self.user = self.storage
        self.membership = self.storage
        self.group = self.storage
        self.budget = self.storage


class ServiceFactory:
    def __init__(self, storages: StorageFactory):
        self.user = UserService(storages.user)
        self.membership = MembershipService(storages.membership)
        self.group = GroupService(storages.group)
        self.summary = SummaryService()
        self.budget = BudgetService(storages.budget)


class HandlerFactory:
    def __init__(self, services: ServiceFactory):
        self.health = HealthHandler()
        self.user = UserHandler(services.user)
        self.membership = MembershipHandler(services.membership)
        self.group = GroupHandler(services.group)
        self.summary = SummaryHandler(services.summary)
        self.budget = BudgetHandler(services.budget)


class AppFactory:
    def __init__(self):
        self.storages = StorageFactory()
        self.services = ServiceFactory(self.storages)
        self.handlers = HandlerFactory(self.services)


def create_factory():
    mode = os.environ.get('IFM_SERVER_MODE', 'simple')
    '''
    Load config by mode
    '''
    return AppFactory()
