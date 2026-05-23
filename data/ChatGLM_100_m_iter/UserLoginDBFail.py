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
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        self.connection.commit()
        return None

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        """
        self.cursor.execute("SELECT * FROM users WHERE username =?", (username,))
        result = self.connection.fetchall()
        return result

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.search_user_by_username('user1')
        """
        self.cursor.execute("DELETE FROM users WHERE username =?", (username,))
        self.connection.commit()
        return None

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.search_user_by_username('user1')
        True
        """
        # Connect to the database
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Insert the user into the database
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        self.connection.commit()

        # Search for the user in the database
        self.cursor.execute("SELECT * FROM users WHERE username =?", (username,))
        result = self.connection.fetchall()

        # Check if the user is found
        if result:
            # If the user is found, check if the password is correct
            if username in result:
                # If the password is correct, the user can log in
                return True
            else:
                # If the password is incorrect, the user cannot log in
                return False
        else:
            # If the user is not found, the user cannot log in
            return False