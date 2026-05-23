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
        return self.current_temperature

    def set_target_temperature(self, temperature):
        self.target_temperature = temperature

    def get_mode(self):
        current_mode = self.mode
        return current_mode

    def set_mode(self, mode):
        current_mode = self.mode
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
        """
        current_temperature = self.current_temperature
        target_temperature = self.target_temperature
    
        if current_temperature < target_temperature:
            self.set_mode('heat')
        else:
            self.set_mode('cool')
    
        return True

    def simulate_operation(self):
        current_temperature = self.current_temperature
        target_temperature = self.target_temperature
    
        if current_temperature < target_temperature:
            self.set_mode('heat')
        else:
            self.set_mode('cool')
    
        while current_temperature != target_temperature:
            if self.auto_check_conflict():
                self.auto_set_mode()
            time.sleep(1)
            current_temperature = self.current_temperature
    
        return 0