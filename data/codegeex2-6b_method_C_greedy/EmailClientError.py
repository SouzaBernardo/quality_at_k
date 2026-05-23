from datetime import datetime
class EmailClient: 
    def __init__(self, addr, capacity) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox = []



    def send_to(self, recv, content, size):
        

        if self.is_full_with_one_more_email(size):
            return False
        else:
            self.inbox.append({'sender': self.addr, 'receiver': recv, 'content': content, 'size': size, 'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'state': 'unread'})
            return True


    def fetch(self):


    def is_full_with_one_more_email(self, size):


    def get_occupied_size(self):
        

        return sum(email['size'] for email in self.inbox)


    def clear_inbox(self, size):