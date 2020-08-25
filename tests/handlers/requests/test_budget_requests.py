import unittest

from server.handlers.requests.budget import CreateBudgetRequest


class TestCreateBudgetRequest(unittest.TestCase):
    def test_init(self):
        good_entry = {
            'name': 'test',
            'percentage': 42.42,
            'builds': True
        }
        bad_entry = {
            'name': 'bad test',
            'percentage': 66.6
        }
        req_dict = {
            'entries': [good_entry]
        }
        with self.assertRaises(TypeError):
            CreateBudgetRequest(**req_dict)

        req_dict['projectedIncome'] = 555.55
        req_dict['entries'] = [bad_entry]
        with self.assertRaises(TypeError):
            CreateBudgetRequest(**req_dict)

        req_dict['entries'] = [good_entry, good_entry]
        req = CreateBudgetRequest(**req_dict)
        self.assertEqual(2, len(req.entries))

        req_dict['fakeArgument'] = 'I should not be here'
        with self.assertRaises(TypeError):
            CreateBudgetRequest(**req_dict)
