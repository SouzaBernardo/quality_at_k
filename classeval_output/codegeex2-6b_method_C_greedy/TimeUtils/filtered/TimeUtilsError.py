import datetime
import time
class TimeUtils: 
    def __init__(self):
        """
        Get the current datetime
        """
        self.datetime = datetime.datetime.now()



    def get_current_time(self):
        

        return self.datetime.strftime("%H:%M:%S")


    def get_current_date(self):
        

        return self.datetime.strftime("%Y-%m-%d")


    def add_seconds(self, seconds):


    def string_to_datetime(self, string):
        

        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


    def datetime_to_string(self, datetime):


    def get_minutes(self, string_time1, string_time2):


    def get_format_time(self, year, month, day, hour, minute, second):