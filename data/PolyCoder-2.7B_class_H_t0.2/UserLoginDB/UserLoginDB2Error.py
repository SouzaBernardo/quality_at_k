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


    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """


    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """


    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.validate_user_login('user1', 'pass1')
        True
        """


    def get_user_by_username(self, username):
        """
        Retrieves a user from the "users" table by username.
        :param username: str, the username of the user to retrieve.
        :return: tuple, the row from the "users" table that matches the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.get_user_by_username('user1')
        ('user1', 'pass1')
        """


    def get_user_by_email(self, email):
        """
        Retrieves a user from the "users" table by email.
        :param email: str, the email of the user to retrieve.
        :return: tuple, the row from the "users" table that matches the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.get_user_by_email('user1@example.com')
        ('user1', 'pass1')
        """


    def get_user_by_username_and_email(self, username, email):
        """
        Retrieves a user from the "users" table by username and email.
        :param username: str, the username of the user to retrieve.
        :param email: str, the email of the user to retrieve.
        :return: tuple, the row from the "users" table that matches the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.get_user_by_username_and_email('user1', 'user1@example.com')
        ('user1', 'pass1')
        """


    def get_user_by_username_and_email_or_username(self, username, email):
        """
        Retrieves a user from the "users" table by username and email.
        :param username: str, the username of the user to retrieve.
        :param email: str, the email of the user to retrieve.
        :return: tuple, the row from the "users" table that matches the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.get_user_by_username_and_email_or_username('user1', 'user1@example.com')
        ('user1', 'pass1')
        """


    def get_user_by_username_or_email(self, username, email):
        """
        Retrieves a user from the "users" table by username and email.
        :param username: str, the username of the user to retrieve.
        :param email: str, the email of the user to retrieve.
        :return: tuple, the row from the "users" table that matches the search criteria.
        >>> user_db = UserLoginDB("user_database.db")