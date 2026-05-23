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
        

        self.cursor.execute()

        self.connection.commit()


    def add_book(self, title, author):
        

        self.cursor.execute("INSERT INTO books VALUES (?, ?, 1)", (title, author))
        self.connection.commit()


    def remove_book(self, book_id):


    def borrow_book(self, book_id):


    def return_book(self, book_id):


    def search_books(self):
        

        books = []
        for row in self.cursor.execute("SELECT * FROM books"):
            books.append(row)
        return books
