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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books (





    def borrow_book(self, book_id):
        self.cursor.execute("UPDATE books SET borrowed = 1 WHERE id =?", (book_id,))
        self.connection.commit()

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        self.cursor.execute("UPDATE books SET status ='returned' WHERE id =?", (book_id,))
        self.connection.commit()

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books