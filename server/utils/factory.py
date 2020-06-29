import os

from server.handlers.health import HealthHandler
from server.handlers.user import UserHandler
from server.services.user import UserService
from server.storage.simple import SimpleStorage


class StorageFactory:
    def __init__(self):
        self.storage = SimpleStorage()
        self.user = self.storage


class ServiceFactory:
    def __init__(self, storages: StorageFactory):
        self.user = UserService(storages.user)


class HandlerFactory:
    def __init__(self, services: ServiceFactory):
        self.health = HealthHandler()
        self.user = UserHandler(services.user)


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
