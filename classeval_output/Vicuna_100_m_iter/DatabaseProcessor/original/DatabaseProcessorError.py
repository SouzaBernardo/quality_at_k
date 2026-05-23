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
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS %s (%s INTEGER PRIMARY KEY, %s %s)""" % (table_name, key1, key2, key1))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def insert_into_database(table_name, data):
        """
        Insert data into the specified table in the database.
    
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("""INSERT INTO %s (%s) VALUES (%s)""" % (table_name, key1, key2))
            for row in data:
                c.execute("""INSERT INTO %s (%s, %s) VALUES (%s, %s)""" % (table_name, key1, key2, key1, row[key1]))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def search_database(self, table_name, name):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("""SELECT * FROM %s WHERE %s = %s""" % (table_name, key1, key2))
            rows = c.fetchall()
            conn.close()
            return rows
        except Exception as e:
            print(e)

