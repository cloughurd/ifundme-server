import unittest

import tests.helpers.setup as setup
from tests.helpers.factory import create_simple_factory, clean_simple_factory


class TestGroupFlow(unittest.TestCase):
    def test_create_group(self):
        filename = 'test-gf-storage.pickle'
        factory = create_simple_factory(filename)
        group_name = 'gf-group'
        setup.create_group(factory, group_name)
        clean_simple_factory(filename)
