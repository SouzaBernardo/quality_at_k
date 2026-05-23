Here is the completed `BookManagement` class:
```python
class BookManagement:
    """
    This is a class as managing books system, which supports to add and remove books from inventory, view the inventory, and check the quantity of a specific book.
    """

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
            self.inventory[quantity] = 1
        self.inventory[title] += quantity

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if quantity not in self.inventory:
            raise ValueError("Invalid quantity for book: %s" % quantity)
        if quantity == 0:
            self.inventory.pop(title, 0)

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int),...}
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
        return self.inventory.get(title, 0)
```
To use this class, you can create an instance of it and add or remove books from the `inventory` dictionary as shown in the `add_book` and `remove_book` methods. You can then view the current inventory and check the quantity of a specific book using the `view_book_quantity` method.