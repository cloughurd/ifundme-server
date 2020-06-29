import os

from server.handlers.health import HealthHandler
from server.handlers.user import UserHandler


class HandlerFactory:
    def __init__(self):
        self.health = HealthHandler()
        self.user = UserHandler()


class AppFactory:
    def __init__(self):
        self.handlers = HandlerFactory()


def create_factory():
    mode = os.environ.get('IFM_SERVER_MODE', 'local')
    '''
    Load config by mode
    '''
    return AppFactory()
