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
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return current_time

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        current_date = self.datetime.strftime("%Y-%m-%d")
        return current_date


    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        current_time = datetime.datetime.now()
        current_time += datetime.timedelta(seconds=seconds)
        current_time = current_time.strftime("%H:%M:%S")
        return current_time

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        try:
            datetime_obj = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
            return datetime_obj
        except ValueError:
            raise ValueError("Invalid date format")

    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
        try:
            if datetime.year < 1900:
                return datetime.strftime("%Y-%m-%d")
            else:
                return datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            raise ValueError("Invalid date format")

    def get_minutes(self, string_time1, string_time2):
            """
            Calculate how many minutes have passed between two times, and round the results to the nearest
            :return: int, the number of minutes between two times, rounded off
            >>> timeutils = TimeUtils()
            >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
            60
            """
            time1 = datetime.datetime.strptime(string_time1, '%Y-%m-%d %H:%M:%S')
            time2 = datetime.datetime.strptime(string_time2, '%Y-%m-%d %H:%M:%S')
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
        >>> timeutils = TimeUtils()
        >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
        "2001-07-18 01:01:01"
        """
        if year < 1900:
            year = str(year)
        else:
            year = str(year).zfill(4)

        if month < 1 or month > 12:
            raise ValueError("Invalid month")

        if day < 1 or day > 31:
            raise ValueError("Invalid day")

        if hour < 0 or hour > 23:
            raise ValueError("Invalid hour")

        if minute < 0 or minute > 59:
            raise ValueError("Invalid minute")

        if second < 0 or second > 59:
            raise ValueError("Invalid second")

        if hour == 0 and minute == 0 and second == 0:
            return "now"

        if hour == 12 and minute == 0 and second == 0:
            return "12:00 PM"

        if hour == 12 and hour % 24 == 0:
            return "12:00 PM"

        if hour == 12 and hour % 24 != 0:
            return "1:00 PM"

        if hour > 12 and hour < 24:
            return f"{hour}:{minute}:"

        if hour == 24 and minute == 0 and second == 0:
            return "11:59 PM"

        if hour == 24 and hour % 24 == 0:
            return "11:59 PM"

        if hour == 24 and hour % 24 != 0:
            return "12:00 AM"

        if minute == 60 and second == 0:
            return "1:00:00"

        if minute == 60 and minute % 60 == 0:
            return "1:00:00"

        if minute == 60 and minute % 60 != 0:
            return f"{minute:02d}:{second:02d}"

        if second == 60 and second % 60 == 0:
            return f"{minute:02d}:{second:02d}"

        if second == 60 and second % 60 != 0:
            return f"{minute:02d}:{second:02d}"

        if hour < 10:
            return f"{hour:02d}"

        if hour >= 10 and hour < 12:
            return f"{hour:02d}:"

        if hour >= 12 and hour < 14:
            return f"{hour:02d}:"

        if hour >= 14 and hour < 16:
            return f"{hour:02d}:"

        if hour >= 16 and hour < 20:
            return f"{hour:02d}