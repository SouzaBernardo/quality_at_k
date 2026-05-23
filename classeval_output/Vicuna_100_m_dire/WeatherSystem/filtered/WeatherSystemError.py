class WeatherSystem: 
    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}







    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
    
        :return: the temperature in Fahrenheit, float.
        """
        if self.temperature is None:
            raise ValueError("Temperature is not set.")
        if self.temperature in self.weather_list:
            return self.weather_list[self.temperature]
        else:
            return 0.0

    def fahrenheit_to_celsius(self):
        if self.temperature is None:
            return None
        return (9/5) * (self.temperature - 32)