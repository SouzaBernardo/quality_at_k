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
        pass


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
        book_id = self.add_book_to_db(title, author)
        self.borrow_book(book_id)
        return book_id


    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        self.connection.execute("DELETE FROM book WHERE id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag WHERE book_id =?", (book_id,))
        self.cursor.execute("DELETE FROM book_book_tag_tag_tag_tag_tag_tag_tag_tag_tag_tag_

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        self.cursor.execute("""
            INSERT INTO books (title, author) VALUES (?,?)
            """, (book_id, "John Smith"))
        self.cursor.execute("""
            UPDATE books SET borrowed = 1
            WHERE id =?
            """, (book_id,))


    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        self.cursor.execute("""
            UPDATE books
            SET book_id = %s
            WHERE book_id = %s
        """, (book_id, book_id))


    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
        books = []
        self.cursor.execute("SELECT * FROM books")
        for row in self.cursor.fetchall():
            books.append( (row[0], row[1], row[2], row[3]) )
        return books
