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





    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        sql = "INSERT INTO books (title, author, availability) VALUES (?,?,?)"
        values = (title, author, 1)
        self.cursor.execute(sql, values)
        self.connection.commit()



    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        sql = "UPDATE books SET availability = 0 WHERE id =?"
        values = (book_id,)
        self.cursor.execute(sql, values)
        self.connection.commit()