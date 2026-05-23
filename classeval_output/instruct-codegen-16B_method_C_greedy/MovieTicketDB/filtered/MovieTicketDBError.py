import sqlite3
class MovieTicketDB: 
    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()




    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    movie_name TEXT,
    theater_name TEXT,
    seat_number TEXT,
    customer_name TEXT



    def search_tickets_by_customer(self, customer_name):
        """
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """
        query = "SELECT * FROM tickets WHERE customer_name =?"
        result = self.cursor.execute(query, (customer_name,))
        return result