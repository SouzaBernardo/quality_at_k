
class CurrencyConverter: 
    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }



    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        """
        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]
        if amount > 0:
            return amount * (to_rate - from_rate)
        else:
            return 0.0



    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        """
        if currency in self.rates:
            raise ValueError("Currency '{}' already supported".format(currency))
        self.rates[currency] = rate
        return None

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
        if currency not in self.rates:
            return False
        if new_rate not in self.rates[currency]:
            return False
        rate = self.rates[currency][new_rate]
        if rate is None:
            return False
        self.rates[currency] = rate