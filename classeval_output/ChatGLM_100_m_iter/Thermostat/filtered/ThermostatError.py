import time
class Thermostat:  
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
    """

    def __init__(self, current_temperature, target_temperature, mode):
        """
        initialize instances of the Thermostat class, including the current temperature, target temperature, and operating mode.
        :param current_temperature: float
        :param target_temperature: float
        :param mode: str, the work mode
        """
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature
        self.mode = mode



    def get_target_temperature(self):
        """
        Get the target temperature of an instance of the Thermostat class.
        :return self.current_temperature: int
        """
        return self.current_temperature

    def set_target_temperature(self, temperature):
        """
        Set the target temperature
        :param temperature: float, the target temperature
        :return: None
        """
        if temperature < self.target_temperature:
            self.mode = "on"
        elif temperature > self.target_temperature:
            self.mode = "off"
        else:
            self.current_temperature = temperature
            self.set_current_temperature_and_mode(temperature, self.mode)

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, working mode. only ['heat', 'cool']
        """
        return self.mode

    def set_mode(self, mode):
        """
        Get the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        :return: None
        """
        if mode == "heat":
            self.current_temperature = 32
            self.set_current_temperature_and_mode(self.current_temperature, "on")
        elif mode == "cool":
            self.current_temperature = 18
            self.set_current_temperature_and_mode(self.current_temperature, "off")

    def auto_set_mode(self):
        """
        Automatically set the operating mode by comparing with the current temperature and target temperature. If the current temperature is lower than the target temperature, the operating mode is set to 'heat', otherwise it is set to 'cool'.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_set_mode()
        >>> thermostat.mode
        'heat'
        """
        if self.current_temperature < self.target_temperature:
            self.mode = "on"
        elif self.current_temperature > self.target_temperature:
            self.mode = "off"
        else:
            self.current_temperature = self.target_temperature
            self.set_current_temperature_and_mode(self.current_temperature, self.mode)