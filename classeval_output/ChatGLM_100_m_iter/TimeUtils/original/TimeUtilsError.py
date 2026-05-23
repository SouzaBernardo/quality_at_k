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
        >>> timeutils = TimeUtils()
        >>> timeutils.get_current_time()
        "19:19:22"
        """
        return datetime.datetime.now().strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        return datetime.datetime.now().strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        self.datetime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        return self.datetime.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        datetime.datetime(2001, 7, 18, 1, 1, 1)
        """
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        """
        return datetime.datetime.strptime(datetime, "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        """
        start_datetime = datetime.datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
        duration = end_datetime - start_datetime
        minutes = duration.seconds // 60
        if minutes > 0:
            return round(minutes * 60)
        else:
            return 0

