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
        Get the names of all tables in the database.
        :return: list, a list of strings representing the names of all tables.
        >>> db.get_table_names()
        ['user', 'user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix(self, prefix):
        """
        Get the names of all tables in the database that match the specified prefix.
        :param prefix: str, the prefix of the tables to search.
        :return: list, a list of strings representing the names of all tables that match the specified prefix.
        >>> db.get_table_names_by_prefix('user')
        ['user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_name(self, prefix, name):
        """
        Get the names of all tables in the database that match the specified prefix and name.
        :param prefix: str, the prefix of the tables to search.
        :param name: str, the name of the table to search for.
        :return: list, a list of strings representing the names of all tables that match the specified prefix and name.
        >>> db.get_table_names_by_prefix_and_name('user', 'John')
        ['user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_name_and_type(self, prefix, name, type):
        """
        Get the names of all tables in the database that match the specified prefix and name and type.
        :param prefix: str, the prefix of the tables to search.
        :param name: str, the name of the table to search for.
        :param type: str, the type of the table to search for.
        :return: list, a list of strings representing the names of all tables that match the specified prefix and name and type.
        >>> db.get_table_names_by_prefix_and_name_and_type('user', 'John', 'user')
        ['user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_name_and_type_and_name(self, prefix, name, type, name_1):
        """
        Get the names of all tables in the database that match the specified prefix and name and type and name 1.
        :param prefix: str, the prefix of the tables to search.
        :param name: str, the name of the table to search for.
        :param type: str, the type of the table to search for.
        :param name_1: str, the name of the table to search for.
        :return: list, a list of strings representing the names of all tables that match the specified prefix and name and type and name 1.
        >>> db.get_table_names_by_prefix_and_name_and_type_and_name('user', 'John', 'user', 'John')
        ['user_name', 'user_name_1', 'user_name_2']
        """


    def get_table_names_by_prefix_and_name_and_type_and_name_1(self, prefix, name, type, name_1, name_2):
        """
        Get the names of all tables in the database that match the specified prefix and name and type and name 1 and name 2.
        :param prefix: str, the prefix of the tables to search.
        :param name: str, the name of the table to search for.
        :param type: str, the type of the table to search for.
        :param name_1: str, the name of the table to search for.
        :param name_