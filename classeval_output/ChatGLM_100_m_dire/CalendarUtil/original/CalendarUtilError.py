from datetime import datetime, timedelta
class CalendarUtil: 
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        self.events = []



    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar,dict.
        :return: A dictionary containing information about the added event,such as the date and time it should be displayed on the calendar.
        """
        # Validate the event data
        if event['date'] < datetime.now().date() or event['date'] > datetime.now().date() + timedelta(days=365):
            raise ValueError(f"Event date must be in the past or future")
        if event['start_time'] < datetime.now().time() or event['start_time'] > datetime.now().time() + timedelta(hours=24):
            raise ValueError(f"Event start time must be in the past or future")
        if event['end_time'] < datetime.now().time() or event['end_time'] > datetime.now().time() + timedelta(hours=24):
            raise ValueError(f"Event end time must be in the past or future")
        # Add the event to the calendar
        calendar.events.append({
            'date': event['date'],
           'start_time': event['start_time'],
            'end_time': event['end_time'],
            'description': event['description']
        })
        return {'events': calendar.events}

    def remove_event(event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        :return: A new empty list of events that were removed from the calendar.
        """
        # Remove the event from the calendar
        del calendar.events[event['date']]
        # Return a new empty list of events that were removed from the calendar
        return []

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        events = []
        for event in self.events:
            if event['date'] == date:
                events.append(event)
        return events

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        if start_time <= end_time:
            return False
        else:
            return True



    def get_upcoming_events(self, date, n):
        """
        Get the next n upcoming events from a given date.
        :param date: The date to get upcoming events from,datetime.
        :param n: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        >>> calendar = CalendarUtil()
        >>> calendar.events = [{'date': datetime(2023, 1, 1, 0, 0),'start_time': datetime(2023, 1, 1, 0, 0), 'end_time': datetime(2023, 1, 1, 23, 0), 'description': 'New Year'},{'date': datetime(2023, 1, 2, 0, 0),'end_time': datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]
        >>> calendar.get_upcoming_events(1)
        [{'date': datetime.datetime(2023, 1, 1, 0, 0),'start_time': datetime.datetime(2023, 1, 1, 0, 0), 'end_time': datetime.datetime(2023, 1, 1, 23, 0), 'description': 'New Year'}, {'date': datetime.datetime(2023, 1, 2, 0, 0),'start_time': datetime.datetime(2023, 1, 2, 0, 0), 'end_time': datetime.datetime(2023, 1, 2, 1, 0), 'description': 'New Year 2'}]

        """
        return [event for event in self.events if event.date == date]