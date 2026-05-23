from datetime import datetime, timedelta
class CalendarUtil: 
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        self.events = []



    def add_event(self, event):
        """
        :param event: The event to be added to the calendar,dict.
        >>> calendar = CalendarUtil()
        >>> calendar.add_event({'date': datetime(2023, 1, 1, 0, 0),'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 1, 0), 'description': 'New Year'})
        >>> calendar.events
        [{'date': datetime.datetime(2023, 1, 1, 0, 0),'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 1, 0), 'description': 'New Year'}]



    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        return [event for event in self.events if date in (event['date'], event['date'].date())]



    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        available_slots = []
        for event in self.events:
            # Check if the event is on the given date
            if event['date'].date() == date.date():
                # Get the start and end time of the event
                start_time = event['start_time']
                end_time = event['end_time']
                # Check if the event is not in the past
                if start_time.date() >= date.date():
                    # Check if the event is not already over
                    if end_time.date() >= date.date():
                        # Check if the event is not in the future
                        if start_time.date() <= date.date():
                            # Add the available time slot to the list
                            available_slots.append((max(start_time, date), min(end_time, date)))
        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        # Get the current date
        current_date = datetime.now()
        # Get the next n upcoming events
        upcoming_events = []
        for event in self.events:
            # Check if the event has already passed
            if current_date < event['date']:
                # Add the event to the list
                upcoming_events.append(event)
        # Return the list of upcoming events
        return upcoming_events[:num_events]