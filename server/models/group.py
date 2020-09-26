from server.utils.ids import IdGenerator


class Group:
    def __init__(self, group_name, group_pin, date_created=None):
        self.group_name = group_name
        self.group_pin = group_pin
        self.date_created = date_created
