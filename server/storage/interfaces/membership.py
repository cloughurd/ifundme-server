from server.models.membership import Membership


class MembershipStorage:
    def search_memberships(self, search_type: str, search_id: str) -> list:
        raise NotImplementedError

    def create_membership(self, username: str, group_name: str, member_type: str) -> Membership:
        raise NotImplementedError

    def update_membership(self, membership_id: str, change_field: str, change_value: str) -> Membership:
        raise NotImplementedError
