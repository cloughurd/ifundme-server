from server.models.user import User


class UserStorage:
    def create_user(self, username: str, password_hash: str) -> User:
        raise NotImplementedError

    def update_user(self, username: str) -> User:
        raise NotImplementedError

    def list_users(self) -> list:
        raise NotImplementedError
