import os
from datetime import date

import pymysql
from pymysql import OperationalError

from server.exceptions.storage import ConnectionException, ResourceAccessException
from server.handlers.requests.budget import BudgetRequestEntry
from server.models.budget import Fund, Category, Income
from server.models.group import Group
from server.models.membership import Membership
from server.models.user import User
from server.storage.interfaces.budget import BudgetStorage
from server.storage.interfaces.group import GroupStorage
from server.storage.interfaces.membership import MembershipStorage
from server.storage.interfaces.user import UserStorage


class MySqlStorage(GroupStorage, UserStorage, MembershipStorage, BudgetStorage):
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

    # TODO: Jordan, write the MySQL code for all the functions
    def create_group(self, group_name, group_pin) -> Group:
        g = Group(group_name, group_pin, date.today())
        sql = '''
            INSERT INTO `groups` 
                (group_name, group_pin, date_created)
                VALUE (%s, %s, %s);
        '''
        val = (g.group_name, g.group_pin, g.date_created)
        try:
            self._execute_insert_query(sql, val)
        except Exception as e:
            raise ResourceAccessException(g.group_name, e)
        return g

    def create_user(self, username: str, password_hash: str) -> User:
        pass

    def update_user(self, username: str) -> User:
        pass

    def list_users(self) -> list:
        pass

    def search_memberships(self, search_type: str, search_id: str) -> list:
        pass

    def create_membership(self, username: str, group_name: str, member_type: str) -> Membership:
        pass

    def update_membership(self, membership_id: str, change_field: str, change_value: str) -> Membership:
        pass

    def get_income(self, group_name: str) -> Income:
        pass

    def list_budget_categories(self, group_name: str) -> list:
        pass

    def create_income(self, group_name: str, projected_income: float) -> Income:
        pass

    def create_budget_category(self, group_name: str, entry: BudgetRequestEntry) -> Category:
        pass

    def create_fund(self, category_id: str, balance=0) -> Fund:
        pass

    def _execute_insert_query(self, sql, val):
        # self.logger.info(self._make_info_log('db-insert', sql, (str(i) for i in val)))
        c = self.db.cursor()
        c.execute(sql, val)
        self.db.commit()

    def _execute_update_statement(self, sql, val):
        # self.logger.info(self._make_info_log('db-update', sql, (str(i) for i in val)))
        c = self.db.cursor()
        c.execute(sql, val)
        self.db.commit()

    def _execute_select_query(self, sql, val):
        # self.logger.info(self._make_info_log('db-select', sql, (str(i) for i in val)))
        c = self.db.cursor()
        c.execute(sql, val)
        return c.fetchone()

    def _execute_select_many_query(self, sql, val):
        # self.logger.info(self._make_info_log('db-select-many', sql, (str(i) for i in val)))
        c = self.db.cursor()
        c.execute(sql, val)
        return c.fetchall()

    def _create_tables(self):
        create_groups_statement = """
            CREATE TABLE IF NOT EXISTS `groups` (
                group_name varchar(48) NOT NULL,
                group_pin varchar(8) NOT NULL,
                date_created date NOT NULL,
                PRIMARY KEY (group_name)
            );  
        """
        create_users_statement = """
            CREATE TABLE IF NOT EXISTS `users` (
                username varchar(48) NOT NULL,
                password_hash varchar(256) NOT NULL,
                date_created date NOT NULL,
                date_last_accessed date NOT NULL,
                PRIMARY KEY (username)
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
                    REFERENCES `users`(username),
                FOREIGN KEY (group_id)
                    REFERENCES `groups`(group_name)
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
                    REFERENCES `groups`(group_name)
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
                    REFERENCES `groups`(group_name)
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
