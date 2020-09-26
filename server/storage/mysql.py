import os

import pymysql
from pymysql import OperationalError

from server.exceptions.storage import ConnectionException


class MySqlStorage:
    def __init__(self, name='server', host=None, user=None, password=None):
        try:
            if host is None:
                host = os.environ.get('IFM_MYSQL_HOST', 'localhost')
            self.host = host
            if user is None:
                user = os.environ['IFM_MYSQL_USER']
            if password is None:
                password = os.environ['IFM_MYSQL_PASSWORD']
            self.db = pymysql.connections.Connection(host=host, user=user, password=password, database=name)
            # self.logger = logging.getLogger(__name__)
            self._create_tables()
            # self.logger.info('[event=sql-storage-started]')
        except KeyError as e:
            raise ConnectionException(e)
        except OperationalError as e:
            raise ConnectionException(e)

    def is_healthy(self):
        try:
            self.db.ping()
        except Exception as e:
            raise ConnectionException(self.host, e)

    def _create_tables(self):
        create_groups_statement = """
            CREATE TABLE IF NOT EXISTS `groups` (
                group_id varchar(48) NOT NULL,
                group_name varchar(48) NOT NULL,
                group_pin varchar(8) NOT NULL,
                date_created date NOT NULL,
                PRIMARY KEY (group_id)
            );  
        """
        create_users_statement = """
            CREATE TABLE IF NOT EXISTS `users` (
                user_id varchar(48) NOT NULL,
                username varchar(48) NOT NULL,
                password_hash varchar(256) NOT NULL,
                date_created date NOT NULL,
                date_last_accessed date NOT NULL,
                PRIMARY KEY (user_id)
            );
        """
        create_memberships_statement = """
            CREATE TABLE IF NOT EXISTS `memberships` (
                membership_id varchar(48) NOT NULL,
                user_id varchar(48) NOT NULL,
                group_id varchar(48) NOT NULL,
                member_type varchar(8) NOT NULL,
                date_created date NOT NULL,
                PRIMARY KEY (membership_id),
                FOREIGN KEY (user_id)
                    REFERENCES `users`(user_id),
                FOREIGN KEY (group_id)
                    REFERENCES `groups`(group_id)
            );
        """
        create_categories_statement = """
            CREATE TABLE IF NOT EXISTS `categories` (
                category_id varchar(48) NOT NULL,
                category_name varchar(48) NOT NULL,
                group_id varchar(48) NOT NULL,
                percentage float NOT NULL,
                date_created date NOT NULL,
                date_updated date NOT NULL,
                PRIMARY KEY (category_id),
                FOREIGN KEY (group_id)
                    REFERENCES `groups`(group_id)
            );
        """
        create_funds_statement = """
            CREATE TABLE IF NOT EXISTS `funds` (
                fund_id varchar(48) NOT NULL,
                category_id varchar(48) NOT NULL,
                balance float NOT NULL,
                date_created date NOT NULL,
                date_updated date NOT NULL,
                PRIMARY KEY (fund_id),
                FOREIGN KEY (category_id)
                    REFERENCES `categories`(category_id)
            );
        """
        create_incomes_statement = """
            CREATE TABLE IF NOT EXISTS `incomes` (
                income_id varchar(48) NOT NULL,
                group_id varchar(48) NOT NULL,
                amount float NOT NULL,
                date_created date NOT NULL,
                date_updated date NOT NULL,
                PRIMARY KEY (income_id),
                FOREIGN KEY (group_id)
                    REFERENCES `groups`(group_id)
            );
        """
        c = self.db.cursor()
        print('Creating groups')
        c.execute(create_groups_statement)
        print('Creating users')
        c.execute(create_users_statement)
        print('Creating memberships')
        c.execute(create_memberships_statement)
        print('Creating categories')
        c.execute(create_categories_statement)
        print('Creating funds')
        c.execute(create_funds_statement)
        print('Creating incomes')
        c.execute(create_incomes_statement)
        print('Tables created')
