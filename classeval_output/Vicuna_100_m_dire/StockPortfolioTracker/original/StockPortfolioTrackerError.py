
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
        self.portfolio.append(stock)


    def remove_stock(self, stock):
        if stock["name"] not in self.portfolio:
            return False
        del self.portfolio[stock["name"]]
        return True

    def buy_stock(self, stock: dict, quantity: int) -> bool:
        """
        Buy a stock and add it to the portfolio.
    
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if self.cash_balance >= quantity * stock["price"]:
            self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": quantity})
            self.cash_balance -= quantity * stock["price"]
            return True
        else:
            return False

    def sell_stock(self, stock, quantity):
        stock_value = 0
        for item in self.portfolio:
            if item["name"] == stock["name"]:
                stock_value = item["price"] * quantity
                self.remove_stock(stock)
                self.cash_balance += quantity * stock["price"]
                return True
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
        total_value = 0.0
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])
    

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
    
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        stock_value = 0.0
        for item in self.portfolio:
            if item["name"] == stock["name"]:
                stock_value = item["price"] * stock["quantity"]
                break
        return stock_value