from datetime import datetime, timedelta
class CalendarUtil:  
    """
    This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        self.events = []



    def add_event(self, event):
        """
        :param event: The event to be added to the calendar,dict.
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        :param event: The event to be removed from the calendar,dict.
        """
        self.events.remove(event)



    def is_available(self, start_time, end_time):
        """
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        for event in self.events:
            if event['start_time'] < end_time and event['end_time'] > start_time:
                return False
        return True

    def get_available_slots(self, date):
        """
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        available_slots = []
        for event in self.events:
            if event['date'] == date:
                start_time = event['start_time']
                end_time = event['end_time']
                while start_time < end_time:
                    available_slots.append((start_time, start_time + timedelta(hours=1)))
                    start_time += timedelta(hours=1)
        return available_slots