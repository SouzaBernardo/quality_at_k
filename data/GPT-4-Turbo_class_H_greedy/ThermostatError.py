import time

class Thermostat:
    """
    The class manages temperature control, including setting and retrieving the target temperature, adjusting the mode, and simulating temperature operation.
    """

    def __init__(self, current_temperature, target_temperature, mode):
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
            raise ValueError("Invalid mode. Only 'heat' and 'cool' are allowed.")

    def auto_set_mode(self):
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'

    def auto_check_conflict(self):
        if (self.mode == 'heat' and self.current_temperature < self.target_temperature) or \
           (self.mode == 'cool' and self.current_temperature > self.target_temperature):
            return True
        else:
            self.auto_set_mode()
            return False

    def simulate_operation(self):
        start_time = time.time()
        self.auto_set_mode()
        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                self.current_temperature += 1
            else:
                self.current_temperature -= 1
            time.sleep(1)
        end_time = time.time()
        return int(end_time - start_time)