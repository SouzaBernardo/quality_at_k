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
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, %s TEXT, %s INTEGER)""" % (table_name, key1, key2))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
    
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        # code to insert data into database using sqlite3 and pandas
        pass

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
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM " + table_name + " WHERE name = ?", (name,))
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return data
        except Exception as e:
            print(e)
            return None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM {} WHERE {} = ?".format(table_name, name))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)