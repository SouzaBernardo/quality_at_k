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