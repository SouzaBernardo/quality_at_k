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
        
        self.cursor.execute()
        self.connection.commit()




    def insert_movie(self, movie_name, theater_name, seat_number, customer_name):


    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        




    def search_movie(self, movie_name):


    def search_tickets_by_customer(self, customer_name):


    def delete_ticket(self, ticket_id):