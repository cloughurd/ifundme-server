from server.models.group import Group


class GroupStorage:
    def create_group(self, group_name, group_pin) -> Group:
        raise NotImplementedError
