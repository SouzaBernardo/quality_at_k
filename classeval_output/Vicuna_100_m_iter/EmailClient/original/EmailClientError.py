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
        # Check if the receiver's email box is full
        if self.check_space(recv):
            return False
    
        # Add the email to the receiver's inbox
        self.inbox.append({
            'recv': recv,
            'content': content,
            'size': size,
            'time': datetime.now(),
            'state': 'unread'
        })
    
        return True



    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False
    
        """
        if len(self.inbox) >= self.capacity and size > 0:
            return True
        return False

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        total_size = 0
        for item in self.inbox:
            size = sum(item['size'])
            total_size += size
        return total_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        if self.is_full_with_one_more_email(size):
            self.inbox = self.inbox[:-1]
            return True
        return False