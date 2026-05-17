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
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender':'sender@example.com','receiver':'receiver@example.com', 'content': 'Hello','size': 10, 'time': '2023-07-13 11:36:40','state': 'unread'}

        """
        if not self.inbox:
            self.inbox = []
        if recv not in self.inbox:
            self.inbox.append(recv)
            self.inbox.append(content)
            self.inbox.append(size)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(self.addr)
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)
            self.inbox.append(datetime.now())
            self.inbox.append(self.capacity)

    def fetch(