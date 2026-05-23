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
        return self.current_temperature

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        mode = self.mode
        return mode

    def set_mode(self, mode):
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError("Invalid mode. Only 'heat' and 'cool' are allowed.")

    def auto_set_mode(self):
        current_temperature = self.current_temperature
        target_temperature = self.target_temperature
    
        if current_temperature < target_temperature:
            self.set_mode('heat')
        else:
            self.set_mode('cool')

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
        if self.current_temperature < self.target_temperature:
            if self.mode == 'heat':
                self.set_mode('cool')
            elif self.mode == 'cool':
                self.set_mode('heat')
        elif self.current_temperature > self.target_temperature:
            if self.mode == 'heat':
                self.set_mode('cool')
            elif self.mode == 'cool':
                self.set_mode('heat')
        return True

    def simulate_operation(self):
        """
        simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
        current_temperature = self.current_temperature
        target_temperature = self.target_temperature
        mode = self.mode

        while current_temperature != target_temperature:
            if mode == 'cool':
                current_temperature -= 1
            elif mode == 'heat':
                current_temperature += 1
            else:
                current_temperature += 0.5

        return current_temperature