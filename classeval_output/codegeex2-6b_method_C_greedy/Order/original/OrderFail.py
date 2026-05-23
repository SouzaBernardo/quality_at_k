
class Order: 
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
                    item["count"] -= dish["count"]
                    self.selected_dishes.append(dish)
                    self.sales[dish["dish"]] = dish["price"] * dish["count"]
                    return True
                else:
                    return False
        self.selected_dishes.append(dish)
        self.sales[dish["dish"]] = dish["price"] * dish["count"]
        return True


    def calculate_total(self):


    def checkout(self):
