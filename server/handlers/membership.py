from abc import ABC

from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase
from server.services.membership import MembershipService


class MembershipHandler(HandlerBase, ABC):
    def __init__(self, service: MembershipService):
        self.service = service

    def search(self, r: Request, **kwargs):
        body = r.get_json()
        try:
            search_type = body['searchType']
            search_id = body['searchId']
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
        if search_type not in ['username', 'group']:
            raise InvalidRequestException(f"search type '{search_type}' not supported")
        memberships = self.service.search(search_type, search_id)
        return {
            'memberships': [m.to_response() for m in memberships]
        }

    def create(self, r: Request, **kwargs):
        body = r.get_json()
        try:
            username = body['username']
            group_name = body['groupName']
            member_type = body['memberType']
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
        membership = self.service.create(username, group_name, member_type)
        return membership.to_response()

    def update(self, r: Request, **kwargs):
        body = r.get_json()
        try:
            membership_id = kwargs['membership_id']
            change_field = body['changeField']
            change_value = body['changeValue']
        except KeyError as e:
            msg = f'{e.args[0]} not provided'
            raise InvalidRequestException(msg, e)
        if change_field not in ['type']:
            raise InvalidRequestException(f"updating '{change_field}' not supported")
        membership = self.service.update(membership_id, change_field, change_value)
        return membership.to_response()
