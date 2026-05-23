from datetime import datetime
class EmailClient:  
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space
    """

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
        """
        if self.inbox.count(recv) > size:
            return False
        self.inbox.append(recv)
        try:
            self.send_from_email(recv)
            return True
        except:
            return False

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        inbox = self.inbox
        first_unread = inbox.values().first()
        if first_unread:
            first_unread.state ='read'
        return first_unread

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        if self.inbox.count(recv) > size:
            return False
        self.inbox.append(recv)
        try:
            self.send_from_email(recv)
            return True
        except:
            return False

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        inbox = self.inbox
        total_size = len(inbox)
        return total_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        :return: True if the email box has enough space, False otherwise.
        """
        if self.inbox.count(recv) > size:
            return False
        for email in inbox:
            if email.state == 'unread':
                del email.state
                inbox.remove(email)
                if len(inbox) < size:
                    return False
        self.inbox = []
        return True