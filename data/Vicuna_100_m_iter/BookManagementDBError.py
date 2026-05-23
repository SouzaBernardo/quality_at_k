import sqlite3
class BookManagementDB:  
    """
    This is a database class as a book management system, used to handle the operations of adding, removing, updating, and searching books.
    """

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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            ISBN TEXT,
            publisher TEXT,
            publication_date TEXT,
            price REAL
        );
        """)
        self.connection.commit()

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.connection.commit()

    def remove_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id):
        self.cursor.execute("UPDATE books SET availability=availability-1 WHERE id=?", (book_id,))
        self.connection.commit()

    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET availability=availability+1 WHERE id=?", (book_id,))
        self.connection.commit()

    def search_books(self):
        cursor = self.cursor
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return [book for book in books]