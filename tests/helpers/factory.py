import os

from server.storage.simple import SimpleStorage
from server.utils.factory import AppFactory


def create_simple_factory(filename: str) -> AppFactory:
    storage = SimpleStorage(filename)
    return AppFactory(storage)


def clean_simple_factory(filename: str):
    os.remove(filename)
