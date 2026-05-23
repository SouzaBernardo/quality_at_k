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
        :return: float, the target temperature
        """
        return self.target_temperature
    

    def set_target_temperature(self, temperature):
        """
        Set the target temperature
        :param temperature: float, the target temperature
        """
        self.target_temperature = temperature
    

    def get_mode(self):
        """
        Get the current work mode
        :return mode: str, working mode. only ['heat', 'cool']
        """
        return self.mode

    def set_mode(self, mode):
        """
        Set the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
        self.mode = mode
    

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'
    

    def auto_check_conflict(self):
        """
        Check if there is a conflict between the operating mode and the relationship between the current temperature and the target temperature.
        If there is a conflict, the operating mode will be adjusted automatically.
        :return: True if mode isn't conflict with the relationship between the current temperature and the target temperature, or False otherwise.
        """
        if self.mode == 'cool' and self.current_temperature >= self.target_temperature:
            self.mode = 'heat'
            return False
        elif self.mode == 'heat' and self.current_temperature <= self.target_temperature:
            self.mode = 'cool'
            return False
        else:
            return True
    

    def simulate_operation(self):
        self.auto_set_mode()  # Step 1

        time_counter = 0  # Initialize the time counter

        while True:  # Step 2
            if self.current_temperature == self.target_temperature:  # Step 3
                break

            if self.current_temperature < self.target_temperature:  # Step 4
                self.current_temperature += 0.5
            else:  # Step 5
                self.current_temperature -= 0.5

            time.sleep(1)  # Step 6
            time_counter += 1  # Increment the time counter

        return time_counter  # Step 8