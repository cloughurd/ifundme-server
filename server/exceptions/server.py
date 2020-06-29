class ServerException(Exception):
    def __init__(self, inner_error=None):
        self.inner_error = inner_error

    def get_message(self):
        return 'A server error occurred'

    def get_code(self):
        return 500

    def to_response(self):
        return {
            'errorMessage': self.get_message(),
            'errorCode': self.get_code()
        }


class InvalidRequestException(ServerException):
    def __init__(self, cause='unknown', inner_error=None):
        super().__init__(inner_error)
        self.cause = cause

    def get_message(self):
        return f'The request was invalid: {self.cause}'

    def get_code(self):
        return 400
