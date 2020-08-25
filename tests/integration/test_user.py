import unittest

import tests.helpers.setup as setup
from tests.helpers.factory import create_simple_factory, clean_simple_factory


class TestUserFlow(unittest.TestCase):
    def test_create_user(self):
        filename = 'test-uf-storage.pickle'
        factory = create_simple_factory(filename)
        username_1 = 'uf-user'
        setup.create_user(factory, username_1)
        clean_simple_factory(filename)
