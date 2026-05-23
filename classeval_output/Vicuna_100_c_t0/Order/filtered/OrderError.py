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