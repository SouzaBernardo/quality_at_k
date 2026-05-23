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


    def get_supported_currencies(self):


    def add_currency_rate(self, currency, rate):
        

        if currency in self.rates:
            return False
        else:
            self.rates[currency] = rate
            return None


    def update_currency_rate(self, currency, new_rate):
        

        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
        return None