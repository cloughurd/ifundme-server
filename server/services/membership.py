from server.handlers.requests.membership import CreateMembershipRequest
from server.storage.interfaces.membership import MembershipStorage


class MembershipService:
    def __init__(self, storage: MembershipStorage):
        self.storage = storage

    def search(self, search_type: str, search_id: str):
        memberships = self.storage.search_memberships(search_type, search_id)
        return sorted(memberships, key=lambda x: x.group_name)

    def create(self, create_membership_request: CreateMembershipRequest):
        # TODO: use group PINs
        memberships = self.storage.search_memberships('username', create_membership_request.username)
        for m in memberships:
            if m.group_name == create_membership_request.group_name:
                return m
        # TODO: pass in whole request object
        new_m = self.storage.create_membership(
            create_membership_request.username,
            create_membership_request.group_name,
            create_membership_request.member_type)
        return new_m

    def update(self, membership_id: str, change_field: str, change_value: str):
        m = self.storage.update_membership(membership_id, change_field, change_value)
        return m
