import json
import unittest
from pathlib import Path

from server.exceptions.server import InvalidRequestException
from server.handlers.requests.budget import CreateBudgetRequest


class TestCreateBudgetRequest(unittest.TestCase):
    def test_init(self):
        example_path = Path(__file__).parents[3] / 'docs' / 'examples' / 'createBudget.json'
        with open(example_path, 'r') as f:
            good_body = json.load(f)

        req = CreateBudgetRequest(**good_body)
        self.assertEqual(4, len(req.categories))
        
        bad_entry = {
            'categoryName': 'bad test',
            'percentage': 66.6
        }
        bad_body = good_body.copy()
        bad_body.pop('projectedIncome')
        with self.assertRaises(KeyError):
            CreateBudgetRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['projectedIncome'] = -42
        with self.assertRaises(InvalidRequestException):
            CreateBudgetRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['projectedIncome'] = 'not a number'
        with self.assertRaises(InvalidRequestException):
            CreateBudgetRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['fakeArgument'] = 'I should not be here'
        with self.assertRaises(InvalidRequestException):
            CreateBudgetRequest(**bad_body)

        bad_body = good_body.copy()
        bad_body['categories'] = bad_body['categories'].copy()
        bad_body['categories'].append(bad_entry)
        print(bad_body)
        with self.assertRaises(KeyError):
            CreateBudgetRequest(**bad_body)

        bad_body = good_body.copy()
        bad_entry['builds'] = 'not a boolean'
        bad_body['categories'] = bad_body['categories'].copy()
        bad_body['categories'].append(bad_entry)
        with self.assertRaises(InvalidRequestException):
            CreateBudgetRequest(**bad_body)
