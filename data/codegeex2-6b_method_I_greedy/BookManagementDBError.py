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
        
        self.cursor.execute()
        self.connection.commit()


    def add_book(self, title, author, year, isbn):





    def remove_book(self, book_id):


    def borrow_book(self, book_id):
        


    def return_book(self, book_id):


    def return_book(self, book_id):


    def search_books(self):