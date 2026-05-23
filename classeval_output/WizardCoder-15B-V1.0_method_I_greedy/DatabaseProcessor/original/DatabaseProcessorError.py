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
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, {} TEXT, {} INTEGER)'''.format(table_name, key1, key2))
        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        for row in data:
            c.execute("INSERT INTO {} (name, age) VALUES (?,?)".format(table_name), (row['name'], row['age']))
        conn.commit()
        conn.close()
    



    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("DELETE FROM {} WHERE name =?".format(table_name), (name,))
        conn.commit()
        conn.close()