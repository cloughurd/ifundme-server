from server.models.user import User


class UserStorage:
    def create(self, username: str, password_hash: str) -> User:
        raise NotImplementedError

    def update(self, username: str) -> User:
        raise NotImplementedError

    def list(self) -> list:
        raise NotImplementedError
