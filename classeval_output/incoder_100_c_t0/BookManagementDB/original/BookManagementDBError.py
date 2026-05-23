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
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
        sql_create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            availability INTEGER
        );
        """
        self.cursor.execute(sql_create_books_table)

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
        sql_add_book = """
        INSERT INTO books (title, author, availability)
        VALUES (?, ?, ?)
        """
        self.cursor.execute(sql_add_book, (title, author, 1))
        self.connection.commit()

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        sql_remove_book = """
        DELETE FROM books
        WHERE book_id = ?
        """
        self.cursor.execute(sql_remove_book, (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        sql_return_book = """
        UPDATE books
        SET availability = 0
        WHERE book_id = ?
        """
        self.cursor.execute(sql_return_book, (book_id,))
        self.connection.commit()

    def search_book(self, book_id):
        """
        Retrieves a book from the database based on the given book ID.
        :param book_id: int
        :return book: tuple, the information of the book
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.search_book(1)
        (2, 'book2', 'author', 2)
        """
        sql_search_book = """
        SELECT * FROM books
        WHERE book_id = ?
        """
        self.cursor.execute(sql_search_book, (book_id,))
        book = self.cursor.fetchone()
        return book

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        sql_return_book = """
        UPDATE books
        SET availability = 1
        WHERE book_id = ?
        """
        self.cursor.execute(sql_return_book, (book_id,))
        self.connection.commit()

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
        sql_search_book = """
        SELECT * FROM books
        """
        self.cursor.execute(sql_search_book)
        books = self.cursor.fetchall()
        return books

    def search_books_by_title(self, title):
        """
        Retrieves all books from the database that match the given title.
        :param title: str
        :return books: list[tuple], the information of all books in database that match the given title
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.search_books_by_title('book1')
        [(1, 'book1', 'author', 1)]
        """
        sql_search_book = """
        SELECT * FROM books
        WHERE title = ?
        """
        self.cursor.execute(sql_search_book, (title,))
        books = self.cursor.fetchall()
        return books

    def search_books_by_author(self, author):
        """
        Retrieves all books from the database that match the given author.
        :param author: str
        :return books: list[tuple], the information of all books in database that match the given author
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.search_books_by_author('author')
        [(1, 'book1', 'author', 1)]
        """
        sql_search_book = """
        SELECT * FROM books
        WHERE author = ?
        """
        self.cursor.execute(sql_search_book, (author,))
        books = self.cursor.fetchall()
        return books

    def search_books_by_availability(self, availability):
        """
        Retrieves all books from the database that match the given availability.
        :param availability: int
        :return books: list[tuple], the information of all books in database that match the given availability
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.search_books_by_availability(1)
        [(1, 'book1', 'author', 1)]
        """
        sql_search_book = """
        SELECT * FROM books
        WHERE availability = ?
        """
        self.cursor.execute(sql_search_book, (availability,))
        books = self.cursor.fetchall()
        return books

<|/ file |>
