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
        email = {
            'sender': self.addr,
            'receiver': recv.addr,
            'content': content,
            'size': size,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'state': 'unread'
        }
    
        if recv.is_full_with_one_more_email(size):
            return False
    
        recv.inbox.append(email)
        return True

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None
    

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        occupied_size = self.get_occupied_size()
        if occupied_size + size > self.capacity:
            return True
        else:
            return False
    

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        total_size = 0
        for email in self.inbox:
            total_size += email['size']
        return total_size
    

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        while self.get_occupied_size() + size > self.capacity:
            oldest_email = min(self.inbox, key=lambda email: email['timestamp'])
            self.inbox.remove(oldest_email)
    