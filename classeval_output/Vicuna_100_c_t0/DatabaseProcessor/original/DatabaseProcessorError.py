```python
from sqlite3 import Error
from pandas import DataFrame

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name
        try:
            self.connect()
        except Error as e:
            print(e)

    def connect(self):
        """
        Connect to the database
        """
        try:
            conn = sqlite3.connect(self.database_name)
            print("Connected to the database")
        except Error as e:
            print(e)

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    %s TEXT,
                    %s INTEGER
                )
            """, (table_name, key1, key2))
            conn.commit()
            print("Table created successfully")
        except Error as e:
            print(e)

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
        try:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO %s (%s, %s)
                VALUES (?, ?, ?)
            """, data)
            conn.commit()
            print("Data inserted successfully")
        except Error as e:
            print(e)

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
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, %s, %s FROM %s WHERE %s = %s
            """, (table_name, key1, key2, table_name, name))
            rows = cursor.fetchall()
            if rows:
                return [row for row in rows]
            else:
                return None
        except Error as e:
            print(e)

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        try:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM %s WHERE %s = %s
            """, (table_name, key1, name))
            conn.commit()
            print("Rows deleted successfully")
        except Error as e: