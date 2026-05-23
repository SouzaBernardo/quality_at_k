from datetime import datetime, timedelta
class CalendarUtil: 
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        self.events = []



    def add_event(self, event):
        """
        :param event: The event to be added to the calendar,dict.
        """
        if 'date' not in event or'start_time' not in event or 'end_time' not in event or 'description' not in event:
            raise ValueError('Event dictionary should have date, start_time, end_time, and description keys.')
        self.events.append(event)

    def remove_event(self, event):
        """
        :param event: The event to be removed from the calendar,dict.
        """
        self.events.remove(event)

    def get_events(self, date):
        """
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        events = []
        for event in self.events:
            if event['date'].date() == date.date():
                events.append(event)
        return events

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
        if not self.events:
            available_slots.append((datetime.combine(date, datetime.min.time()), datetime.combine(date + timedelta(days=1), datetime.min.time())))
        else:
            for event in self.events:
                if event['date'].date() == date.date():
                    start_time = max(event['start_time'], datetime.combine(date, datetime.min.time()))
                    end_time = min(event['end_time'], datetime.combine(date + timedelta(days=1), datetime.min.time()))
                    if not available_slots or end_time > available_slots[-1][1]:
                        available_slots.append((start_time, end_time))
                    else:
                        available_slots[-1] = (available_slots[-1][0], end_time)
            if not available_slots or available_slots[-1][1] < datetime.combine(date + timedelta(days=1), datetime.min.time()):
                available_slots.append((datetime.combine(date + timedelta(days=1), datetime.min.time()), datetime.combine(date + timedelta(days=2), datetime.min.time())))
        return available_slots

    def get_upcoming_events(self, num_events):
        """
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        upcoming_events = []
        for event in self.events:
            if event['date'] >= datetime.now().date() and len(upcoming_events) < num_events:
                upcoming_events.append(event)
        return upcoming_events