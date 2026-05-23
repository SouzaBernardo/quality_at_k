from datetime import datetime
class Chat: 
    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}







    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        """
        if sender not in self.users or receiver not in self.users:
            return False
        else:
            self.users[sender].append({
           'sender': sender,
           'receiver': receiver,
           'message': message,
            'timestamp': datetime.now()
        })
            return True

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys'sender','receiver','message', 'timestamp'.
        """
        messages = []
        for message in self.users[username]:
            messages.append(message)
        return messages