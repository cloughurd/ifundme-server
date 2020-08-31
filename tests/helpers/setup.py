from server.models.membership import Membership
from server.utils.factory import AppFactory
from server.utils.constants import RequestBodyKeys
from tests.helpers.request import DummyRequest


def _add_entry_or_default(dictionary, key, value, default):
    if value is not None:
        dictionary[key] = value
    if key not in dictionary:
        dictionary[key] = default
    return dictionary


def create_user(factory: AppFactory, username=None, body=None):
    if body is None:
        body = {}
    body = _add_entry_or_default(body, RequestBodyKeys.username, username, 'test user')
    return factory.handlers.user.create(DummyRequest().with_body(body))


def create_group(factory: AppFactory, group_name=None, body=None):
    if body is None:
        body = {}
    body = _add_entry_or_default(body, RequestBodyKeys.group_name, group_name, 'test group')
    return factory.handlers.group.create(DummyRequest().with_body(body))


def create_membership(factory: AppFactory, username=None, group_name=None, member_type=None, body=None):
    if body is None:
        body = {}
    body = _add_entry_or_default(body, RequestBodyKeys.username, username, 'test user')
    body = _add_entry_or_default(body, RequestBodyKeys.group_name, group_name, 'test group')
    body = _add_entry_or_default(body, RequestBodyKeys.member_type, member_type, Membership.normal_type)
    return factory.handlers.membership.create(DummyRequest().with_body(body))


def create_budget(factory: AppFactory, group_name=None, projected_income=None, entries=None, body=None):
    if body is None:
        body = {}
    default_entries = [{ 'name': 'general', 'percentage': 100.0, 'builds': True}]
    body = _add_entry_or_default(body, RequestBodyKeys.entries, entries, default_entries)
    body = _add_entry_or_default(body, RequestBodyKeys.projected_income, projected_income, 1000.0)
    return factory.handlers.budget.create(DummyRequest().with_body(body), group_name=group_name)
