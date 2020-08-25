class DummyRequest:
    def __init__(self):
        self.body = {}

    def with_body(self, body):
        self.body = body
        return self

    def get_json(self):
        return self.body
