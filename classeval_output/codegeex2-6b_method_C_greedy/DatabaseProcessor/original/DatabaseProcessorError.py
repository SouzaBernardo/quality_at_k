import sqlite3
import pandas as pd
class DatabaseProcessor: 
    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name




    def create_table(self, table_name, key1, key2):


    def insert_into_database(self, table_name, data):


    def search_database(self, table_name, name):
        

        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("SELECT * FROM {} WHERE name = '{}'".format(table_name, name))
        result = c.fetchall()
        conn.close()
        return result


    def delete_from_database(self, table_name, name):
