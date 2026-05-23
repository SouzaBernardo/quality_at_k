import sqlite3
class BookManagementDB: 
    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor, 
        and creates the book table if it does not already exist
        :param db_name: str, the name of db file
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()



    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                author TEXT NOT NULL,
                                borrowed INTEGER DEFAULT 0
                            )''')
        self.connection.commit()
    

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        query = "INSERT INTO book (title, author, availability) VALUES (?, ?, 1)"
        self.cursor.execute(query, (title, author))
        self.connection.commit()
    

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        """
        query = "DELETE FROM book WHERE id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
    

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        # Execute an SQL query to update the status of the book with the given book ID
        query = "UPDATE book SET status = 'Borrowed' WHERE id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
    

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        query = "UPDATE book SET borrowed = 0 WHERE id = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()
    

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        self.cursor.execute("SELECT * FROM book")
        books = self.cursor.fetchall()
        return books