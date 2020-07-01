from datetime import date

from server.utils.ids import IdGenerator


class Membership:
    leader_type = 'leader'
    normal_type = 'member'

    def __init__(self, username, group_name, member_type, date_created=None, membership_id=None):
        self.username = username
        self.group_name = group_name
        self.member_type = member_type
        self.date_created: date = date_created
        if membership_id is None:
            membership_id = IdGenerator.generate_membership_id()
        self.membership_id = membership_id

    def to_response(self):
        return {
            'membershipId': self.membership_id,
            'username': self.username,
            'groupName': self.group_name,
            'memberType': self.member_type,
            'dateCreated': self.date_created.isoformat()
        }
