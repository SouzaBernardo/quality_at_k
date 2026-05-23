import sqlite3
import pandas as pd
class DatabaseProcessor: 
    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name






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
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            for row in data:
                cursor.execute(f'INSERT INTO {table_name} ({key1}, {key2}) VALUES (?,?)', (row[key1], row[key2]))
            connection.commit()


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
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = f'SELECT * FROM {table_name} WHERE {table_name}.name =?'
            result = cursor.execute(query, (name,)).fetchall()
        return result if result else None


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        query = f'DELETE FROM {table_name} WHERE {key1} =?'
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()