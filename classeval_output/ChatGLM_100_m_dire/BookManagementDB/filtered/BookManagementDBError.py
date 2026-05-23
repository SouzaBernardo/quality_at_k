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
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
        self.connection.commit()

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
        self.connection.commit()
        book = {"id": 1, "title": title, "author": author, "availability": 1}
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?,?)", (book,))
        self.connection.commit()

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        :return: None
        """
        self.cursor.execute("DELETE FROM books WHERE id =?", (book_id,))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        :return: None
        """
        self.cursor.execute("INSERT INTO borrowed_books (book_id, borrowed) VALUES (?,?)", (book_id, True))
        self.connection.commit()
        return None

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        :return: None
        """
        self.cursor.execute("SELECT * FROM books WHERE id =?", (book_id,))
        result = self.connection.fetchone()
        if result:
            self.cursor.execute("INSERT INTO books (title, author) VALUES (?,?)", (result[0], result[1]))
            self.connection.commit()
            print("Book returned with ID", result[0])
        else:
            print("Book not found")

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
        self.cursor.execute("SELECT title, author, id FROM books")
        books = self.cursor.fetchall()
        return books