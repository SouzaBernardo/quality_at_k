import datetime
import time
class TimeUtils:  
    """
    This is a time util class, including getting the current time and date, adding seconds to a datetime, converting between strings and datetime objects, calculating the time difference in minutes, and formatting a datetime object.
    """

    def __init__(self):
        """
        Get the current datetime
        """
        self.datetime = datetime.datetime.now()



    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """
        return self.datetime.strftime('%H:%M:%S')



    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        new_datetime = self.datetime + datetime.timedelta(seconds=seconds)
        return new_datetime.strftime('%H:%M:%S')





    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        """
        time1 = datetime.datetime.strptime(string_time1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.datetime.strptime(string_time2, '%Y-%m-%d %H:%M:%S')
        diff = time2 - time1
        minutes = diff.total_seconds() // 60
        return round(minutes)