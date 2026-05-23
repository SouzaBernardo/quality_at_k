import datetime
import time
class TimeUtils: 
    def __init__(self):
        """
        Get the current datetime
        """
        self.datetime = datetime.datetime.now()



    def get_current_time(self):
        return self.get_current_date() + self.add_seconds(180) + self.string_to_datetime("18:00") + self.datetime_to_string("23:00")

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        self.datetime += datetime.timedelta(seconds=seconds)
        return self.datetime.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        datetime.datetime(2001, 7, 18, 1, 1, 1)
        """
        try:
            return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        except strptimeError:
            return None

    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
        return datetime.datetime.strftime("%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=int(self.get_minutes(datetime.timetuple(datetime.datetime.now().timetuple()), "00", "00"))

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
        current_time = self.get_current_time()
        current_date = self.get_current_date()
        time_diff = self.add_seconds(current_time - string_time2)
        format_time = self.get_format_time(current_date, year, month, day, hour, minute, second)
        minutes = round(time_diff / 60, 2)
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
        return f"{year}-{month}-{day} {hour}:{minute}:{second}"