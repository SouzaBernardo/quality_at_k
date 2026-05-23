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
        """
        if username in self.users:
            return False
        else:
            self.users[username] = []
            return True
    

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        """
        if username in self.users:
            del self.users[username]
            return True
        else:
            return False
    

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        """
        if sender in self.users and receiver in self.users:
            timestamp = datetime.now()
            self.users[receiver].append((sender, message, timestamp))
            return True
        else:
            return False
    

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        messages = []
        for user in self.users.values():
            for message in user:
                if message[0] == username:
                    messages.append({
                        'sender': message[0],
                        'receiver': message[1],
                        'message': message[2],
                        'timestamp': message[3]
                    })
        return messages
    