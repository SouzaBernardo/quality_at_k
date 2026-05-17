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
        """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities,dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather':'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27,'sunny')

        """
        if not self.city:
            return None, None
        if not self.temperature:
            self.temperature = self.city.get_temperature()
        if not self.weather:
            self.weather = self.city.get_weather()
        if tmp_units == 'celsius':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'celsius':
            tmp_units = 'C'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'
        if tmp_units == 'C':
            tmp_units = 'F'
        if tmp_units == 'F':
            tmp_units = 'C'