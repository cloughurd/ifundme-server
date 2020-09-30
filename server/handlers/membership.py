from abc import ABC

from flask import Request

from server.exceptions.server import InvalidRequestException
from server.handlers.base import HandlerBase, respond, handle_key_error
from server.handlers.requests.membership import CreateMembershipRequest
from server.services.membership import MembershipService


class MembershipHandler(HandlerBase, ABC):
    def __init__(self, service: MembershipService):
        self.service = service

    @respond
    @handle_key_error
    def search(self, r: Request, **kwargs):
        body = r.get_json()
        search_type = body['searchType']
        search_id = body['searchId']
        if search_type not in ['username', 'group']:
            raise InvalidRequestException(f"search type '{search_type}' not supported")
        memberships = self.service.search(search_type, search_id)
        return {
            'memberships': [m.to_response() for m in memberships]
        }

    @respond
    @handle_key_error
    def create(self, r: Request, **kwargs):
        body = r.get_json()
        create_membership_request = CreateMembershipRequest(**body)
        membership = self.service.create(create_membership_request)
        return membership.to_response()

    @respond
    @handle_key_error
    def update(self, r: Request, **kwargs):
        body = r.get_json()
        membership_id = kwargs['membership_id']
        change_field = body['changeField']
        change_value = body['changeValue']
        if change_field not in ['type']:
            raise InvalidRequestException(f"updating '{change_field}' not supported")
        membership = self.service.update(membership_id, change_field, change_value)
        return membership.to_response()
