
class DiscountStrategy:  
    """
    This is a class that allows to use different discount strategy based on shopping credit or shopping cart in supermarket.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)

        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()






    def due(self):
        
        if self.promotion == None:
            return self.total()
        else:
            return self.promotion(self)






    def total(self):
        
        self.total_price = 0
        for item in self.cart:
            self.total_price += item['price'] * item['quantity']
        return self.total_price






    def FidelityPromo(self):
        
        if self.customer['fidelity'] >= 1000:
            return self.total() * 0.05
        else:
            return 0






    def BulkItemPromo(self):
        
        if sum(item['quantity'] for item in self.cart) >= 10:
            return self.total() * 0.07
        else:
            return 0






    def LargeOrderPromo(self):
        
        if len(self.cart) >= 10:
            return self.total() * 0.1
        else:
            return 0


@staticmethod
    def FidelityPromo(order):


@staticmethod
    def BulkItemPromo(order):


@staticmethod
    def LargeOrderPromo(order):
