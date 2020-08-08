from abc import ABCMeta

from server.handlers.base import HandlerBase


class HealthHandler(HandlerBase, metaclass=ABCMeta):
    def get(self, **kwargs):
        return {
            'status': 'all is well'
        }
