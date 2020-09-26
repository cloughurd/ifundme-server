from pymysql.connections import Cursor


def cleanup_mysql_tables(c: Cursor):
    c.execute('DROP TABLE `incomes`')
    c.execute('DROP TABLE `funds`')
    c.execute('DROP TABLE `categories`')
    c.execute('DROP TABLE `memberships`')
    c.execute('DROP TABLE `users`')
    c.execute('DROP TABLE `groups`')
