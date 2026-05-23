import sqlite3
class UserLoginDB:  
    """
    This is a database management class for user login verification, providing functions for inserting user information, searching user information, deleting user information, and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()



    def insert_user(self, username, password):
        cursor = self.cursor
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        cursor = self.cursor
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = cursor.fetchall()
        return result

    def delete_user_by_username(self, username):
        cursor = self.cursor
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
            cursor = self.cursor
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if result and result[1] == password:
                return True
            return False