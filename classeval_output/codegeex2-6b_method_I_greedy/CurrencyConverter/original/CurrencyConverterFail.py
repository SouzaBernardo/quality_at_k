
class CurrencyConverter:  
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

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



        """


    def get_supported_currencies(self):
        
        return list(self.rates.keys())


    def add_currency_rate(self, currency_type, rate):


    def add_currency_rate(self, currency, rate):


    def update_currency_rate(self, currency, new_rate):
