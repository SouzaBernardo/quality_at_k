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



        """


    def fetch(self):


    def is_full_with_one_more_email(self, size):


    def get_occupied_size(self):


    def clear_inbox(self, size):