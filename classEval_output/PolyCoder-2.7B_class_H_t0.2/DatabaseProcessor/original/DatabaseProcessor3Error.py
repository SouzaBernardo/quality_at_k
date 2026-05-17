import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """


    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """


    def get_table_names(self):
        """
        Return a list of table names in the database.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names()
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix(self, prefix):
        """
        Return a list of table names in the database matching the specified prefix.
        :param prefix: str, the prefix to match.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names_by_prefix('user')
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_suffix(self, prefix, suffix):
        """
        Return a list of table names in the database matching the specified prefix and suffix.
        :param prefix: str, the prefix to match.
        :param suffix: str, the suffix to match.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names_by_prefix_and_suffix('user', 'user')
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_suffix_and_prefix(self, prefix, suffix, prefix_len):
        """
        Return a list of table names in the database matching the specified prefix and suffix.
        :param prefix: str, the prefix to match.
        :param suffix: str, the suffix to match.
        :param prefix_len: int, the length of the prefix to match.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names_by_prefix_and_suffix_and_prefix('user', 'user', 3)
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_suffix_and_prefix_and_suffix(self, prefix, suffix, prefix_len, suffix, prefix_len):
        """
        Return a list of table names in the database matching the specified prefix and suffix.
        :param prefix: str, the prefix to match.
        :param suffix: str, the suffix to match.
        :param prefix_len: int, the length of the prefix to match.
        :param suffix_len: int, the length of the suffix to match.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names_by_prefix_and_suffix_and_prefix_and_suffix('user', 'user', 3, 3)
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_suffix_and_prefix_and_suffix_and_prefix(self, prefix, suffix, prefix_len, suffix, prefix_len, suffix_len):
        """
        Return a list of table names in the database matching the specified prefix and suffix.
        :param prefix: str, the prefix to match.
        :param suffix: str, the suffix to match.
        :param prefix_len: int, the length of the prefix to match.
        :param suffix_len: int, the length of the suffix to match.
        :param prefix_len: int, the length of the prefix to match.
        :return: list, a list of strings representing the table names.
        >>> db.get_table_names_by_prefix_and_suffix_and_prefix_and_suffix_and_prefix('user