class User:
    def __init__(self, username, password_hash, date_created=None, date_last_accessed=None):
        self.username = username
        self.password_hash = password_hash
        self.date_created = date_created
        self.date_last_accessed = date_last_accessed
