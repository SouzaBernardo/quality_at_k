class WeatherSystem:  
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

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
        temperature = self.temperature
        return temperature * 9/5 + 32

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weatherSystem.temperature = 80.6
        >>> weatherSystem.fahrenheit_to_celsius()
        26.999999999999996

        """
        if self.temperature is None:
            raise ValueError("Temperature is not set.")
        temperature = self.temperature
        return temperature * 9/5 + 32