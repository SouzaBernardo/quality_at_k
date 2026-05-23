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
        """
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS {} (

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        # Create a list of tuples from the data
        data_tuples = [tuple(d.values()) for d in data]
        # Create a list of column names
        column_names = list(data[0].keys())
        # Create a list of placeholders
        placeholders = ["?" for _ in range(len(column_names))]
        # Create the query string
        query_string = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ", ".join(column_names), ", ".join(placeholders))
        # Execute the query
        self.cursor.executemany(query_string, data_tuples)
        # Commit the changes to the database
        self.connection.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        # Create a query string
        query_string = "SELECT * FROM {} WHERE name =?".format(table_name)
        # Execute the query
        self.cursor.execute(query_string, (name,))
        # Fetch all the results
        results = self.cursor.fetchall()
        # Return the results
        return results

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        # Create a query string
        query_string = "DELETE FROM {} WHERE name =?".format(table_name)
        # Execute the query
        self.cursor.execute(query_string, (name,))
        # Commit the changes to the database
        self.connection.commit()