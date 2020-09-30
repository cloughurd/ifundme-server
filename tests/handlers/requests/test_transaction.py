import unittest
import json
from pathlib import Path

from server.exceptions.server import InvalidRequestException
from server.handlers.requests.transaction import CreateTransactionRequest


class TestTransactionRequest(unittest.TestCase):
    def test_init(self):
        example_path = Path(__file__).parents[3] / 'docs' / 'examples' / 'createTransaction.json'
        with open(example_path, 'r') as f:
            good_body = json.load(f)
        CreateTransactionRequest(**good_body)

        bad_body = good_body.copy()
        bad_body['transactionType'] = 'not a real type'
        with self.assertRaises(InvalidRequestException):
            CreateTransactionRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body.pop('amount')
        with self.assertRaises(KeyError):
            CreateTransactionRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['fakeArgument'] = 'I should not be here'
        with self.assertRaises(InvalidRequestException):
            CreateTransactionRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['transactionDate'] = 'I am not a good date'
        with self.assertRaises(InvalidRequestException):
            CreateTransactionRequest(**bad_body)
