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
        >>> thermostat.get_target_temperature()
        37.5
        """

    def set_target_temperature(self, temperature):
        """
        Set the target temperature
        :param temperature: float, the target temperature
        >>> thermostat.set_target_temperature(37.6)
        >>> thermostat.target_temperature
        37.6
        """

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, working mode. only ['heat', 'cool']
        """

    def set_mode(self, mode):
        """
        Get the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """

    def auto_set_mode(self):
        """
        Automatically set the operating mode by comparing with the current temperature and target temperature. If the current temperature is lower than the target temperature, the operating mode is set to 'heat', otherwise it is set to 'cool'.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_set_mode()
        >>> thermostat.mode
        'heat'
        """

    def auto_check_conflict(self):
        """
        Check if there is a conflict between the operating mode and the relationship between the current temperature and the target temperature.
        If there is a conflict, the operating mode will be adjusted automatically.
        :return: True if mode isn't conflict with the relationship between the current temperature and the target temperature, or False otherwise.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_check_conflict()
        False
        >>> thermostat.mode
        'heat'
        """

    def simulate_operation(self):
        """
        simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """

    def get_current_temperature(self):
        """
        Get the current temperature of the Thermostat class.
        :return self.current_temperature: float
        >>> thermostat.get_current_temperature()
        37.5
        """

    def get_target_temperature(self):
        """
        Get the target temperature of the Thermostat class.
        :return self.target_temperature: float
        >>> thermostat.get_target_temperature()
        37.6
        """

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, the work mode
        >>> thermostat.get_mode()
        'cool'
        """

    def get_current_mode(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_current_mode()
        'cool'
        """

    def get_mode_name(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_mode_name()
        'cool'
        """

    def get_mode_name_short(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_mode_name_short()
        'cool'
        """

    def get_mode_name_long(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_mode_name_long()
        'cool'
        """

    def get_mode_name_short_long(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_mode_name_short_long()
        'cool'
        """

    def get_mode_name_long_short(self):
        """
        Get the current work mode
        :return mode: str, the current work mode
        >>> thermostat.get_mode_name_long_short()
        'cool'
        """

    def get_mode_name_short_long_short(self):
        """
        Get the current work mode
        :return mode: str, the