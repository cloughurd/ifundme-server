import unittest

from server.models.membership import Membership
import tests.helpers.setup as setup
from tests.helpers.factory import create_simple_factory, clean_simple_factory


class TestMembershipFlow(unittest.TestCase):
    def test_create_membership(self):
        filename = 'test-mf-storage.pickle'
        factory = create_simple_factory(filename)
        username_1 = 'mf-user-1'
        username_2 = 'mf-user-2'
        group_name = 'mf-group'

        setup.create_user(factory, username_1)
        setup.create_user(factory, username_2)
        setup.create_group(factory, group_name)
        setup.create_membership(factory, username_1, group_name, Membership.leader_type)
        setup.create_membership(factory, username_2, group_name, Membership.normal_type)

        clean_simple_factory(filename)
