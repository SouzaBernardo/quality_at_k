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
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender':'sender@example.com','receiver':'receiver@example.com', 'content': 'Hello','size': 10, 'time': '2023-07-13 11:36:40','state': 'unread'}

        """
        if self.inbox.count(recv) > self.capacity:
            return False
        if self.inbox.count(recv) < size:
            return False
        if self.inbox.count(recv) == size:
            return True
        self.inbox.append(recv)
        return self.send_to_next(recv, content, size)

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        first_unread = self.inbox.pop(0)
        first_unread.state ='read'
        return first_unread

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        if self.inbox.count(size) > 0:
            return True
        else:
            self.inbox.append(size)
            return False

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        inbox = self.inbox
        last_email_size = inbox[-1]['size']
        if last_email_size < capacity:
            return last_email_size
        else:
            return capacity - last_email_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        :return: The email box with all emails deleted.
        """
        if size < self.inbox[-1]['size']:
            self.inbox.pop(-1)
        else:
            self.inbox.pop(0)
        self.inbox.append({'size': size})