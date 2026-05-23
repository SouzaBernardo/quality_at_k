import sqlite3
import pandas as pd
class DatabaseProcessor: 
    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name








    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        query = "SELECT * FROM {} WHERE name='{}'".format(table_name, name)
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE name='{name}'"
        c.execute(query)
        conn.commit()
        conn.close()