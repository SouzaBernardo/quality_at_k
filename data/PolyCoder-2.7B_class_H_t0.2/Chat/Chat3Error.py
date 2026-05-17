from datetime import datetime

class Chat:
    """
    This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.
    """

    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        self.users = {'John': []}
        >>> chat.add_user('John')
        False

        """

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        >>> chat = Chat()
        >>> chat.users = {'John': []}
        >>> chat.remove_user('John')
        True
        >>> chat.remove_user('John')
        False

        """

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Hello')
        True
        >>> chat.send_message('John', 'Tom', 'Hello')
        False

        """

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys'sender','receiver','message', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_messages('John')
        [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_messages('Mary')
        []

        """

    def get_user(self, username):
        """
        Get the user with the given username.
        :param username: The user's name, str.
        :return: If the user is not in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_user('John')
        True
        >>> chat.get_user('Mary')
        False

        """

    def get_users(self):
        """
        Get all the users in the Chat.
        :return: A list of users, each user is a dictionary with keys 'username', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_users()
        [{'username': 'John', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_users()
        []

        """

    def get_all_users(self):
        """
        Get all the users in the Chat.
        :return: A list of users, each user is a dictionary with keys 'username', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_all_users()
        [{'username': 'John', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_all_users()
        []

        """

    def get_all_users_by_username(self, username):
        """
        Get all the users in the Chat.
        :param username: The user's name, str.
        :return: A list of users, each user is a dictionary with keys 'username', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_all_users_by_username('John')
        [{'username': 'John', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_all_users_by_username('Mary')
        []

        """

    def get_all_users_by_username_and_type(self, username, type):
        """
        Get all the users in the Chat.
        :param username: The user's name, str.
        :param type: The type of the user, str.
        :return: A list of users, each user is a dictionary with keys 'username', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John','receiver': 'Mary','message': 'Hello', 'timestamp': '2023-01