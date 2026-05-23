```python
from datetime import datetime

class EmailClient:
    def __init__(self, addr, capacity) -> None:
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    def send_to(self, recv, content, size):
        if recv.is_full_with_one_more_email(size):
            return False
        else:
            recv.inbox.append({'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': size, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'state': 'unread'})
            return True

    def fetch(self):
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email

    def is_full_with_one_more_email(self, size):
        if self.get_occupied_size() + size > self.capacity:
            return True
        else:
            return False

    def get_occupied_size(self):
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size):
        self.inbox.sort(key=lambda x: x['time'])
        while self.get_occupied_size() + size > self.capacity:
            self.inbox.pop(0)
```
This code completes the EmailClient class. The send_to method sends an email to the receiver if the receiver's email box has enough space. The fetch method retrieves the first unread email in the email box and marks it as read. The is_full_with_one_more_email method checks if the email box will be full after adding an email of the given size. The get_occupied_size method returns the total size of the emails in the email box. The clear_inbox method deletes the oldest emails until the email box has enough space to accommodate the given size.