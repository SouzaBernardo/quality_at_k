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
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.cursor.execute(query, (username, password))
        self.connection.commit()
    

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        query = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchall()
        return result
    

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        query = "DELETE FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        self.connection.commit()
    

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        """
        user = self.search_user_by_username(username)
        if user:
            stored_password = user[0][1]  # Assuming the password is stored in the second column of the "users" table
            if password == stored_password:
                return True
        return False