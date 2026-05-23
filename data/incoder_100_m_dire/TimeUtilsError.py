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
        hour = str(self.datetime.hour)
        minute = str(self.datetime.minute)
        second = str(self.datetime.second)
        return hour + ":" + minute + ":" + second


    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")


    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        seconds_str = str(seconds)
        seconds_str = seconds_str.zfill(4)
        seconds_str = seconds_str[0:2] + ":" + seconds_str[2:4] + ":" + seconds_str[4:6]
        self.datetime = self.datetime + datetime.timedelta(seconds=int(seconds))
        return self.datetime_to_string(self.datetime)


    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        year, month, day, hour, minute, second = string.split(' ')
        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))


    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
        datetime_str = datetime.strftime('%Y-%m-%d %H:%M:%S')
        return datetime_str


    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
        string_time1 = string_time1.split(" ")
        string_time2 = string_time2.split(" ")
        year1 = int(string_time1[0])
        month1 = int(string_time1[1])
        day1 = int(string_time1[2])
        hour1 = int(string_time1[3])
        minute1 = int(string_time1[4])
        year2 = int(string_time2[0])
        month2 = int(string_time2[1])
        day2 = int(string_time2[2])
        hour2 = int(string_time2[3])
        minute2 = int(string_time2[4])
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        day1 = day1 + 1
        day2 = day2 + 1
        year1 = year1 - 1900
        year2 = year2 - 1900
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 2000
        year2 = year2 + 2000
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 1900
        year2 = year2 - 1900
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 2000
        year2 = year2 + 2000
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 12
        hour2 = hour2 - 12
        minute1 = minute1 - 30
        minute2 = minute2 - 30
        year1 = year1 + 1900
        year2 = year2 + 1900
        hour1 = hour1 + 12
        hour2 = hour2 + 12
        minute1 = minute1 + 30
        minute2 = minute2 + 30
        year1 = year1 - 2000
        year2 = year2 - 2000
        hour1 = hour1 - 


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
        format_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
        return format_time