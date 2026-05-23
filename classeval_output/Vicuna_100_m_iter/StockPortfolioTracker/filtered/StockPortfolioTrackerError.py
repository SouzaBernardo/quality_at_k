class StockPortfolioTracker:  
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

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
        :return: None
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
        self.portfolio.append(stock)
        self.cash_balance -= stock["price"] * stock["quantity"]

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
    
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock is found in the portfolio, False otherwise
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

    def buy_stock(self, stock, quantity):
        if self.cash_balance >= stock["price"] * quantity:
            self.portfolio.append(stock)
            self.cash_balance -= stock["price"] * quantity
            return True
        else:
            return False

    def sell_stock(self, stock, quantity):
        if self.cash_balance >= stock["price"] * quantity:
            self.portfolio.remove(stock)
            self.cash_balance -= stock["price"] * quantity
            return True
        else:
            return False

    def calculate_portfolio_value(self):
        total_value = 0.0
        for stock in self.portfolio:
            total_value += stock["price"]
        return total_value

    def get_portfolio_summary(self):
        """
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
        total_value = self.calculate_portfolio_value()
        portfolio_value_dict = {}
        for stock in self.portfolio:
            name = stock["name"]
            value = stock["price"]
            if name in portfolio_value_dict:
                portfolio_value_dict[name] += value
            else:
                portfolio_value_dict[name] = value
        return total_value, portfolio_value_dict