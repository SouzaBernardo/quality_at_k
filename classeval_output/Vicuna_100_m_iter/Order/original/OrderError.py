
class Order:  
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}




    def add_dish(self, dish):
        if dish in self.menu:
            if len(self.selected_dishes) < 1:
                self.selected_dishes.append(dish)
                self.menu.append(dish)
                self.sales[dish["dish"]] = dish["price"] * dish["count"]
                return True
            else:
                return False
        else:
            return False

    def calculate_total(self):
        total = 0
        for dish in self.menu:
            if dish in self.sales:
                total += self.sales[dish] * self.selected_dishes.count(dish)
        return total

