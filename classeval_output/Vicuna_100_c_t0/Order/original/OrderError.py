```python
class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        if dish in self.selected_dishes:
            self.menu.append(dish)
            self.sales[dish["dish"]] += dish["count"] * dish["price"]
            self.selected_dishes.remove(dish)
        else:
            self.menu.append(dish)
            self.sales[dish["dish"]] = dish["count"] * dish["price"]

    def calculate_total(self):
        total = 0
        for dish in self.menu:
            total += self.sales[dish]
        return total

    def checkout(self):
        total = self.calculate_total()
        if len(self.selected_dishes) == 0:
            return False
        else:
            return total
```
### Explanation:
The `Order` class is a simple class that manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.

The `__init__` method initializes the order management system by creating an empty `menu` list and an empty `selected_dishes` list, and an empty `sales` dictionary.

The `add_dish` method allows the customer to add dishes to their order by checking if the dish is in the `selected_dishes` list. If it is, it is removed from the list and added to the `menu` list. The count of the dish is added to the `sales` dictionary, and the price of the dish is multiplied by the count to calculate the total cost.

The `calculate_total` method calculates the total cost of all the dishes in the `menu` list by looping through the list and adding the cost of each dish to a `total` variable.

The `checkout` method allows the customer to checkout their order by first checking if the `selected_dishes` list is empty. If it is, the method returns `False` because the customer has not added any dishes to their order. If the list is not empty, the method calculates the total cost of the order by calling the `calculate_total` method and returns it.