import time
class Thermostat: 
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
            self.set_mode(self.mode_auto)
        elif temperature > self.target_temperature:
            self.set_mode(self.mode_high)
        else:
            self.set_mode(self.mode_low)

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, working mode. only ['heat', 'cool']
        """
        if self.mode == "heat":
            return "heat"
        elif self.mode == "cool":
            return "cool"
        else:
            return None

    def set_mode(self, mode):
        """
        Get the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
        if mode not in ['heat', 'cool']:
            print("Invalid mode: {}".format(mode))
            return
        self.current_temperature = self.target_temperature
        self.mode = mode

    def auto_set_mode(self):
        self.mode = self.get_mode() if self.mode else 'heat'