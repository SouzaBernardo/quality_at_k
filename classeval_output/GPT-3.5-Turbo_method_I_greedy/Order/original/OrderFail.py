
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
        for item in self.menu:
            if item["dish"] == dish["dish"]:
                if item["count"] >= dish["count"]:
                    self.selected_dishes.append(dish)
                    item["count"] -= dish["count"]
                    return True
                else:
                    return False
        return False
    

    def calculate_total(self):
        total = 0
        for dish in self.selected_dishes:
            total += dish["count"] * dish["price"] * self.sales[dish["dish"]]
        return total
    

    def checkout(self):
        if not self.selected_dishes:
            return False
        else:
            return self.calculate_total()
    