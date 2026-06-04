class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        """
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)")
        self.conn.commit()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        """
        for row in data:
            self.cursor.execute(f"INSERT INTO {table_name} ({', '.join(row.keys())}) VALUES ({', '.join('?'*len(row))})", tuple(row.values()))
        self.conn.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        """
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE name=?", (name,))
        rows = self.cursor.fetchall()
        return rows if rows else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        """
        self.cursor.execute(f"DELETE FROM {table_name} WHERE name=?", (name,))
        self.conn.commit()