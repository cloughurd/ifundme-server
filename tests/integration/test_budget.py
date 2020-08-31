import unittest

from tests.helpers import setup
from tests.helpers.factory import create_simple_factory, clean_simple_factory


class TestBudgetFlow(unittest.TestCase):
    def test_create_budget(self):
        filename = 'test-bf-storage.pickle'
        factory = create_simple_factory(filename)
        group_name = 'bf-group'
        setup.create_group(factory, group_name)
        setup.create_budget(factory, group_name)
        clean_simple_factory(filename)

    def test_generate_summary(self):
        filename = 'test-sf-storage.pickle'
        factory = create_simple_factory(filename)
        group_name = 'sf-group'
        setup.create_group(factory, group_name)
        setup.create_budget(factory, group_name)
        factory.handlers.summary.get(None, group_name=group_name)
        clean_simple_factory(filename)
