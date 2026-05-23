import sqlite3
import pandas as pd
class DatabaseProcessor: 
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
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)")
        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        # Create a table if it doesn't exist
        c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({key1} TEXT PRIMARY KEY, {key2} TEXT)")

        # Insert data into the table
        for row in data:
            c.execute(f"INSERT INTO {table_name} ({key1}, {key2}) VALUES (?,?)", (row[key1], row[key2]))

        # Commit changes and close the connection
        conn.commit()
        conn.close()


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE name='{name}'")
        result = cursor.fetchall()
        conn.close()
        if result:
            return result
        else:
            return None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"DELETE FROM {table_name} WHERE name=?", (name,))
        conn.commit()
        conn.close()