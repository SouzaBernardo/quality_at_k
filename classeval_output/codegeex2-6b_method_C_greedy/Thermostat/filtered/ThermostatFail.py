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
        

        return self.target_temperature


    def set_target_temperature(self, temperature):
        

        self.target_temperature = temperature


    def get_mode(self):
        
        return self.mode


    def set_mode(self, mode):
        

        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            raise ValueError('mode must be in ["heat", "cool"]')


    def auto_set_mode(self):


    def auto_check_conflict(self):
        

        if self.mode == 'cool' and self.current_temperature > self.target_temperature:
            self.mode = 'off'
            return False
        elif self.mode == 'heat' and self.current_temperature < self.target_temperature:
            self.mode = 'off'
            return False
        else:
            return True


    def simulate_operation(self):