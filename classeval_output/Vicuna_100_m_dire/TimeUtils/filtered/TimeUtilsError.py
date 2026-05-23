import datetime
import time
class TimeUtils: 
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
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return current_time

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return current_date

    def add_seconds(self, seconds):
        current_time = self.datetime.time()
        new_time = current_time + seconds
        return time.strftime("%H:%M:%S", time.localtime(new_time))

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        try:
            dt = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
            return dt.date() + dt.timedelta()
        except ValueError:
            return None

    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
            60
        """
        time1 = datetime.datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
        time_diff = time2 - time1
        minutes = round(time_diff.seconds / 60)
        return minutes

    def get_format_time(self, year, month, day, hour, minute, second):
        """
        get format time
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: formatted time string
        >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
        "2001-07-18 01:01:01"
        """
        formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second}"
        return formatted_time