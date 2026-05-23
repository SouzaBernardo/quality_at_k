
class WeatherSystem: 
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
            return self.celsius_to_fahrenheit(), self.weather
        else:
            return self.fahrenheit_to_celsius(), self.weather


    def set_city(self, city):


    def celsius_to_fahrenheit(self):


    def fahrenheit_to_celsius(self):
