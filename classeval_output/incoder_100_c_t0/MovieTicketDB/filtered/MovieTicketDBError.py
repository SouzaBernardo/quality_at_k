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
            theater_name TEXT,
            seat_number TEXT,
            customer_name TEXT
        );
        """
        self.cursor.execute(sql_command)
        self.connection.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """
        sql_command = """
        INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
        VALUES (?, ?, ?, ?);
        """
        self.cursor.execute(sql_command, (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()

    def search_tickets_by_movie(self, movie_name):
        """
        Searches for tickets in the "tickets" table by movie name.
        :param movie_name: str, the name of the movie to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_movie("Movie A")
        len(result) = 1
        """
        sql_command = """
        SELECT * FROM tickets WHERE movie_name = ?;
        """
        self.cursor.execute(sql_command, (movie_name,))
        return self.cursor.fetchall()

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
        sql_command = """
        SELECT * FROM tickets WHERE customer_name = ?;
        """
        self.cursor.execute(sql_command, (customer_name,))
        return self.cursor.fetchall()

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
        sql_command = """
        DELETE FROM tickets WHERE id = ?;
        """
        self.cursor.execute(sql_command, (ticket_id,))
        self.connection.commit()