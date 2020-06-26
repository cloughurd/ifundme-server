from server.handlers.base import HandlerBase


class HealthHandler(HandlerBase):
    def get(self):
        return True
