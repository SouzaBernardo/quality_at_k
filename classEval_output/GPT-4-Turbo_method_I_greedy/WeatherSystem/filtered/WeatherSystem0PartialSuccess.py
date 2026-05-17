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
        """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities,dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        """
        if self.city in weather_list:
            self.weather = weather_list[self.city]['weather']
            self.temperature = weather_list[self.city]['temperature']
            if tmp_units == 'fahrenheit' and weather_list[self.city]['temperature units'] == 'celsius':
                self.temperature = self.temperature * 9/5 + 32
            elif tmp_units == 'celsius' and weather_list[self.city]['temperature units'] == 'fahrenheit':
                self.temperature = (self.temperature - 32) * 5/9
        return (self.temperature, self.weather)
    def set_city(self, city):
        """
        Set the city of the weather system.
        :param city: the city to set, str.
        :return: None
        """
        self.city = city
    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.
        """
        if self.temperature is not None:
            return self.temperature * 9/5 + 32
        else:
            return None
    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        """
        if self.temperature is not None:
            return (self.temperature - 32) * 5/9
        else:
            return None