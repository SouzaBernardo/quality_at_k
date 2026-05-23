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


    def close_database(self):
        """
        Close the database connection.
        """


    def __enter__(self):
        """
        Open the database connection.
        """
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the database connection.
        """
        self.connection.close()


class DatabaseProcessorTest(unittest.TestCase):
    """
    This is a class for testing the DatabaseProcessor class.
    """


    def test_create_table(self):
        """
        Test the create_table method.
        """
        db = DatabaseProcessor('test.db')
        db.create_table('user', 'name', 'age')
        self.assertEqual(db.cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="user"').fetchone()[0], 'user')
        db.close_database()


    def test_insert_into_database(self):
        """
        Test the insert_into_database method.
        """
        db = DatabaseProcessor('test.db')
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        self.assertEqual(db.cursor.execute('SELECT * FROM user').fetchall(), [
                (1, 'John', 25),
                (2, 'Alice', 30)
            ])
        db.close_database()


    def test_search_database(self):
        """
        Test the search_database method.
        """
        db = DatabaseProcessor('test.db')
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        self.assertEqual(db.search_database('user', 'John'), [(1, 'John', 25)])
        self.assertEqual(db.search_database('user', 'Alice'), [(2, 'Alice', 30)])
        db.close_database()


    def test_delete_from_database(self):
        """
        Test the delete_from_database method.
        """
        db = DatabaseProcessor('test.db')
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        db.delete_from_database('user', 'John')
        self.assertEqual(db.search_database('user', 'John'), None)
        db.close_database()


    def test_close_database(self):
        """
        Test the close_database method.
        """
        db = DatabaseProcessor('test.db')
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        db.close_database()
        self.assertEqual(db.cursor.execute('SELECT * FROM sqlite_master WHERE type="table" AND name="user"').fetchone(), None)
        db.close_database()


if __name__ == '__main__':
    unittest.main()
