from server.storage.membership import MembershipStorage


class MembershipService:
    def __init__(self, storage: MembershipStorage):
        self.storage = storage

    def search(self, search_type: str, search_id: str):
        memberships = self.storage.search_memberships(search_type, search_id)
        return sorted(memberships, key=lambda x: x.group_name)

    def create(self, username: str, group_name: str, member_type: str):
        # TODO: use group PINs
        memberships = self.storage.search_memberships('username', username)
        for m in memberships:
            if m.group_name == group_name:
                return m
        new_m = self.storage.create_membership(username, group_name, member_type)
        return new_m

    def update(self, membership_id: str, change_field: str, change_value: str):
        m = self.storage.update_membership(membership_id, change_field, change_value)
        return m
