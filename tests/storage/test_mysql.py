import unittest
import os

from server.storage.mysql import MySqlStorage


@unittest.skipIf(os.environ.get('IFM_MYSQL_HOST') is None, 'No MySQL host available')
class TestMySqlStorage(unittest.TestCase):
    def test_create_tables(self):
        storage = MySqlStorage(
            name='test',
            host=os.environ['IFM_MYSQL_HOST'],
            user='test',
            password=os.environ['IFM_MYSQL_PASSWORD_TEST']
        )
        storage.is_healthy()
