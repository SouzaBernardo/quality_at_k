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
        :return: None, indicating that the table was created successfully
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT)")
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        :return: None, indicating that the book was added successfully
        """
        self.cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?,?,?)", (title, author, self.get_isbn()))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        :return: None, indicating that the book was removed successfully
        """
        self.cursor.execute("DELETE FROM books WHERE id =?", (book_id,))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        :return: None, indicating that the book was borrowed successfully
        """
        self.cursor.execute("INSERT INTO borrowed_books (book_id, title) VALUES (?,?)", (book_id, self.get_title()))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        :return: None, indicating that the book was returned successfully
        """
        self.cursor.execute("INSERT INTO returned_books (book_id) VALUES (?)", (book_id,))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        books = self.search_by_title(self.get_books(), self.get_author())
        if len(books) == 0:
            return []
        return [book for book in books]