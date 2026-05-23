import sqlite3
class MovieTicketDB:  
    """
    This is a class for movie database operations, which allows for inserting movie information, searching for movie information by name, and deleting movie information by name.
    """

    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()



    def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, author name of type str, seat number of type str, and customer name of type str
        :return: None
        """
        sql_command = """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            movie_name TEXT,
            author_name TEXT,
            seat_number TEXT,
            customer_name TEXT
        )
        """
        self.cursor.execute(sql_command)
        self.connection.commit()
