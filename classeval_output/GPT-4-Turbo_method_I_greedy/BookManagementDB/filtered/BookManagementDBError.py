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
        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT,
            isbn TEXT UNIQUE
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author.
        :param title: str, book title
        :param author: str, author name
        """
        add_book_query = """
        INSERT INTO books (title, author)
        VALUES (?, ?)
        """
        self.cursor.execute(add_book_query, (title, author))
        self.connection.commit()
    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        """
        remove_book_query = """
        DELETE FROM books WHERE id = ?
        """
        self.cursor.execute(remove_book_query, (book_id,))
        self.connection.commit()
    
    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        borrow_book_query = """
        UPDATE books SET borrowed = 1 WHERE id = ?
        """
        self.cursor.execute(borrow_book_query, (book_id,))
        self.connection.commit()
    
    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        return_book_query = """
        UPDATE books SET borrowed = 0 WHERE id = ?
        """
        self.cursor.execute(return_book_query, (book_id,))
        self.connection.commit()
    
    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        search_books_query = """
        SELECT * FROM books
        """
        self.cursor.execute(search_books_query)
        books = self.cursor.fetchall()
        return books