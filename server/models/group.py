from server.utils.ids import IdGenerator


class Group:
    def __init__(self, group_name, group_pin, date_created=None, group_id=None):
        self.group_name = group_name
        self.group_pin = group_pin
        self.date_created = date_created
        if group_id is None:
            group_id = IdGenerator.generate_group_id()
        self.group_id = group_id
