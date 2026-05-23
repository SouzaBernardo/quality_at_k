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
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        for s in self.portfolio:
            if s["name"] == stock["name"]:
                self.portfolio.remove(s)
                return True
        return False

    def buy_stock(self, stock, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if self.cash_balance >= stock["price"] * quantity:
            self.cash_balance -= stock["price"] * quantity
            for s in self.portfolio:
                if s["name"] == stock["name"]:
                    s["quantity"] += quantity
                    return True
            stock["quantity"] = quantity
            self.portfolio.append(stock)
            return True
        return False

    def sell_stock(self, stock, quantity):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        for s in self.portfolio:
            if s["name"] == stock["name"]:
                if s["quantity"] >= quantity:
                    self.cash_balance += stock["price"] * quantity
                    s["quantity"] -= quantity
                    return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        value = 0.0
        for s in self.portfolio:
            value += s["price"] * s["quantity"]
        return value + self.cash_balance

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        value = 0.0
        stocks = []
        for s in self.portfolio:
            stock_value = s["price"] * s["quantity"]
            value += stock_value
            stocks.append({"name": s["name"], "value": stock_value})
        return (value + self.cash_balance, stocks)

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        for s in self.portfolio:
            if s["name"] == stock["name"]:
                return s["price"] * s["quantity"]
        return 0.0