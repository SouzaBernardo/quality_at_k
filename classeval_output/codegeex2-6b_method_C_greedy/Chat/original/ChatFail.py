from datetime import datetime
class Chat: 
    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}



    def add_user(self, username):
        
        if username in self.users:
            return False
        else:
            self.users[username] = []
            return True


    def remove_user(self, username):
        

        if username in self.users:
            del self.users[username]
            return True
        else:
            return False


    def send_message(self, sender, receiver, message):
        

        if sender not in self.users or receiver not in self.users:
            return False

        if receiver not in self.users[sender]:
            self.users[sender].append(receiver)

        if sender not in self.users[receiver]:
            self.users[receiver].append(sender)

        self.users[sender].append(datetime.now())
        self.users[receiver].append(datetime.now())

        self.users[sender].append(message)

        return True


    def get_messages(self, username):
