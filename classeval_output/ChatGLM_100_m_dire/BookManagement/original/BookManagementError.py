
class BookManagement: 
    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}



    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if quantity not in self.inventory:
            self.inventory[quantity] = []
        self.inventory[quantity].append(title)

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if quantity not in self.inventory:
            raise ValueError("Invalid quantity for book: %s" % quantity)
        for book in self.inventory.values():
            if book.get(title) and self.inventory.get(book.get(title)) == quantity:
                self.inventory.pop(book.get(title))



