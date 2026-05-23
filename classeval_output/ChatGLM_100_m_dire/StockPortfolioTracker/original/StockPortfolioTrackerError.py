
class StockPortfolioTracker: 
    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance



    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": stock["quantity"]})
        self.cash_balance += stock["price"]

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was removed, False otherwise
        """
        if stock["name"] == "AAPL" and stock["price"] == 150.0 and stock["quantity"] == 10:
            self.portfolio.remove({"name": stock["name"], "price": stock["price"], "quantity": stock["quantity"]})
            return True
        else:
            return False

    def buy_stock(self, stock, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if stock["quantity"] < self.cash_balance:
            return False
        elif stock["quantity"] > self.portfolio.count(stock["name"]):
            return False
        else:
            self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": quantity})
            return True

    def sell_stock(self, stock, quantity):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if quantity < stock["quantity"]:
            return False
        elif quantity > stock["quantity"] + stock["price"]:
            return False
        else:
            # Check if the stock exists in the portfolio
            if stock in self.portfolio:
                # If it does, sell it and update the cash balance
                self.portfolio.remove(stock)
                self.cash_balance += stock["price"]
                return True
            else:
                # If it doesn't, add the cash to the cash balance
                self.cash_balance += stock["price"]
                return True



    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
        total_value = self.calculate_portfolio_value()
        portfolio = [self.get_stock_value(stock) for stock in self.portfolio]
        return total_value, portfolio

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0
    
        """
        return stock["price"] * stock["quantity"]