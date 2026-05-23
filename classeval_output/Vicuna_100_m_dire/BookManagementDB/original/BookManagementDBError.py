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
        c = self.connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    ISBN TEXT
                    )''')
        self.connection.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.connection.commit()
        print("Book added successfully!")

    def remove_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE books SET borrowed = True WHERE id = ?", (book_id,))
            self.connection.commit()
            print("Book borrowed successfully!")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE books SET status='returned' WHERE id=?", (book_id,))
        self.connection.commit()

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return: list[tuple], the information of all books in database
        """
        cursor = self.cursor
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return [book for book in books]