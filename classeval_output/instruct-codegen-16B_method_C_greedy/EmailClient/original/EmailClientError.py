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





    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender':'sender@example.com','receiver':'receiver@example.com', 'content': 'Hello','size': 10, 'time': '2023-07-13 11:36:40','state': 'unread'}]
        >>> receiver.fetch()
        {'sender':'sender@example.com','receiver':'receiver@example.com', 'content': 'Hello','size': 10, 'time': '2023-07-13 11:36:40','state':'read'}
        """



    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        occupied_size = 0
        for email in self.inbox:
            occupied_size += email['size']
        return occupied_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        while self.get_occupied_size() + size > self.capacity:
            self.inbox.pop(0)
        self.inbox.append({'size': size, 'time': datetime.now()})