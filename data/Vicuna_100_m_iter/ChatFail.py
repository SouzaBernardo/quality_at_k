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
        if username in self.users:
            return False
        self.users[username] = []
        return True

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
        if username in self.users:
            del self.users[username]
            return True
        return False


    def send_message(self, sender, receiver, message):
        if sender not in self.users or receiver not in self.users:
            return False
        self.users[sender].append(receiver)
        self.users[receiver].append(sender)
        return True

    def get_messages(self, username):
        messages = []
        for sender in self.users[username]:
            for receiver in self.users[sender]:
                if receiver != username:
                    messages.append({'sender': sender, 'receiver': receiver, 'message': '', 'timestamp': ''})
        return messages