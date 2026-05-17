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
        Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
        :return: None
        """

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """

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

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """

    def get_ticket(self, ticket_id):
        """
        Gets a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to get.
        :return: tuple, the ticket data, the ticket ID, the ticket name, the ticket seat number, the customer name, and the customer seat number.
        """

    def get_all_tickets(self):
        """
        Gets all tickets from the "tickets" table.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> ticket_db.insert_ticket("Movie B", "Theater 2", "B1", "John Doe")
        >>> ticket_db.insert_ticket("Movie C", "Theater 3", "C1", "John Doe")
        >>> ticket_db.insert_ticket("Movie D", "Theater 4", "D1", "John Doe")
        >>> result = ticket_db.get_all_tickets()
        >>> len(result) = 3
        """

    def get_all_tickets_by_customer(self, customer_name):
        """
        Gets all tickets from the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> ticket_db.insert_ticket("Movie B", "Theater 2", "B1", "John Doe")
        >>> ticket_db.insert_ticket("Movie C", "Theater 3", "C1", "John Doe")
        >>> ticket_db.insert_ticket("Movie D", "Theater 4", "D1", "John Doe")
        >>> ticket_db.insert_ticket("Movie E", "Theater 5", "E1", "John Doe")
        >>> ticket_db.insert_ticket("Movie F", "Theater 6", "F1", "John Doe")
        >>> ticket_db.insert_ticket("Movie G", "Theater 7", "G1", "John Doe")
        >>> ticket_db.insert_ticket("Movie H", "Theater 8", "H1", "John Doe")
        >>> ticket_db.insert_ticket("Movie I", "Theater 9", "I1", "John Doe")
        >>> ticket_db.insert_ticket("Movie J", "Theater 10", "J1", "John Doe")
        >>> ticket_db.insert_ticket("Movie K", "Theater 11", "K1", "John Doe")
        >>> ticket_db.insert_ticket("Movie L", "Theater 12", "L1", "John Doe")
        >>> ticket_db.insert_ticket("Movie M", "Theater 13", "M1", "John Doe")
        >>> ticket_db.insert_ticket("Movie N", "Theater 14", "N1", "John Doe")
        >>> ticket_db.insert_ticket("Movie O", "Theater 15", "O1", "John Doe")
        >>> ticket_db.insert_ticket("Movie P", "Theater 16", "P1", "John Doe")
        >>> ticket_db.insert_ticket("Movie Q", "Theater 17", "Q1", "John Doe")
        >>> ticket_db.insert_ticket("Movie R", "Theater 18", "R1", "John Doe")
        >>> ticket_db.insert_ticket("Movie S", "Theater 19", "S1", "John Doe")
        >>> ticket_db.insert_ticket("Movie T", "Theater 20", "T1", "John Doe")
        >>> ticket_db.insert_ticket("Movie U",