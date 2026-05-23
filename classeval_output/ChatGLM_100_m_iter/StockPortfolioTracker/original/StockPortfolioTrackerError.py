
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
        """
        self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": stock["quantity"]})
        self.cash_balance -= stock["price"]

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        self.portfolio.remove(stock)
        self.cash_balance -= stock["price"]
        return True  # Return True to indicate the stock was removed successfully

    def buy_stock(self, stock, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if quantity > self.portfolio.count(stock["name"]):
            return False  # The stock is already in the portfolio, so we cannot buy it
        
        self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": quantity})
        self.cash_balance -= stock["price"]
        return True

    def sell_stock(self, stock, quantity):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if stock["quantity"] == quantity:
            self.cash_balance += stock["price"]
            return True
        
        self.portfolio.remove(stock)
        self.cash_balance -= stock["price"]
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        11500.0

        """
        return self.calculate_total_value()


    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.calculate_portfolio_value()
        portfolio_summary = (total_value, [])
        for stock in self.portfolio:
            name = stock["name"]
            value = stock["price"]
            portfolio_summary.append({"name": name, "value": value})
        return (total_value, portfolio_summary)

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        return self.calculate_portfolio_value() - stock["price"]