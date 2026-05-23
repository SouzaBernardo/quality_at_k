import sqlite3
class UserLoginDB: 
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
        delete_query = "DELETE FROM users WHERE username = ?"
        self.cursor.execute(delete_query, (username,))
        self.connection.commit()
    

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        """
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
    