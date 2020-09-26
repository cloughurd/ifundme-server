from server.exceptions.server import ServerException


class DuplicateResourceIdException(ServerException):
    def __init__(self, resource_id='unknown', resource_type='uknown', inner_error=None):
        super().__init__(inner_error)
        self.resource_id = resource_id
        self.resource_type = resource_type

    def get_message(self):
        return f"A resource with id '{self.resource_id}' of type '{self.resource_type}' already exists"

    def get_code(self):
        return 400


class StorageAccessException(ServerException):
    def __init__(self, storage_type='unknown', inner_error=None):
        super().__init__(inner_error)
        self.storage_type = storage_type

    def get_message(self):
        return f"Unable to access storage '{self.storage_type}'"


class ResourceNotFoundException(ServerException):
    def __init__(self, resource_id='unknown', resource_type='unknown', inner_error=None):
        super().__init__(inner_error)
        self.resource_id = resource_id
        self.resource_type = resource_type

    def get_message(self):
        return f"The resource '{self.resource_id}' of type '{self.resource_type}' was not found"

    def get_code(self):
        return 404


class ConnectionException(ServerException):
    def __init__(self, host='unknown', inner_error=None):
        super().__init__(inner_error)
        self.host = host

    def get_message(self):
        return f'Unable to connect to {self.host}'


class ResourceAccessException(ServerException):
    def __init__(self, resource_id, inner_error=None):
        super().__init__(inner_error)
        self.resource_id = resource_id

    def get_message(self):
        return 'Problem accessing resource {} in storage'.format(self.resource_id)
