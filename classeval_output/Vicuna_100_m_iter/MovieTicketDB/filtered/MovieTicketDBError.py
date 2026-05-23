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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT,
            author_name TEXT,
            seat_number TEXT,
            customer_name TEXT
        )
        """)
        self.connection.commit()

    def insert_ticket(movie_name, theater_name, seat_number, customer_name):
        # code to insert ticket into the database
        pass

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
        cursor = self.cursor
        cursor.execute("SELECT * FROM tickets WHERE customer_name = ?", (customer_name,))
        return cursor.fetchall()

    def delete_ticket(ticket_id):
        cursor = self.cursor
        cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
        self.connection.commit()