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



    def query(self, weather_list, tmp_units = 'celsius'):
        
        self.weather_list = weather_list
        self.temperature = weather_list[self.city]['temperature']
        self.weather = weather_list[self.city]['weather']
        if tmp_units == 'celsius':
            return self.temperature, self.weather
        elif tmp_units == 'fahrenheit':
            return (self.temperature * 1.8) + 32, self.weather
        else:
            return self.temperature, self.weather


    def set_city(self, city):
        

        self.city = city


    def celsius_to_fahrenheit(self):
        

        return (self.temperature * 1.8) + 32


    def fahrenheit_to_celsius(self):


    def fahrenheit_to_celsius(self):
        

        return (self.temperature - 32) * (5/9)