```python
class Order:
    def __init__(self):
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        for item in self.menu:
            if item["dish"] == dish["dish"]:
                if item["count"] >= dish["count"]:
                    item["count"] -= dish["count"]
                    self.selected_dishes.append(dish)
                    return True
        return False

    def calculate_total(self):
        total = 0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"] * self.sales.get(dish["dish"], 1)
        return total

    def checkout(self):
        if not self.selected_dishes:
            return False
        else:
            total = self.calculate_total()
            self.selected_dishes = []  # clear the selected dishes after checkout
            return total
```