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
        """
        self.events.append(event)
    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar,dict.
        """
        if event in self.events:
            self.events.remove(event)
    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        events_on_date = [event for event in self.events if event['date'].date() == date.date()]
        return events_on_date
    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot,datetime.
        :param end_time: The end time of the time slot,datetime.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """
        for event in self.events:
            if (start_time >= event['start_time'] and start_time < event['end_time']) or \
               (end_time > event['start_time'] and end_time <= event['end_time']) or \
               (start_time <= event['start_time'] and end_time >= event['end_time']):
                return False
        return True
    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for,datetime.
        :return: A list of available time slots on the given date,list.
        """
        # Initialize the start of the day
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        # Initialize the end of the day
        end_of_day = datetime(date.year, date.month, date.day, 23, 59)
    
        # Get all events on the given date
        events_on_date = self.get_events(date)
    
        # Sort the events by start time
        events_on_date.sort(key=lambda x: x['start_time'])
    
        # Initialize the list of available slots
        available_slots = []
    
        # Check the time slot before the first event
        if events_on_date and events_on_date[0]['start_time'] > start_of_day:
            available_slots.append((start_of_day, events_on_date[0]['start_time']))
    
        # Check the time slots between events
        for i in range(len(events_on_date) - 1):
            if events_on_date[i]['end_time'] < events_on_date[i + 1]['start_time']:
                available_slots.append((events_on_date[i]['end_time'], events_on_date[i + 1]['start_time']))
    
        # Check the time slot after the last event
        if events_on_date and events_on_date[-1]['end_time'] < end_of_day:
            available_slots.append((events_on_date[-1]['end_time'], end_of_day))
    
        return available_slots
    
    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :param num_events: The number of upcoming events to get,int.
        :return: A list of the next n upcoming events from the given date,list.
        """
        # Get the current date and time
        now = datetime.now()
    
        # Filter the events that are in the future
        future_events = [event for event in self.events if event['start_time'] > now]
    
        # Sort the future events by start time
        future_events.sort(key=lambda x: x['start_time'])
    
        # Return the first n future events
        return future_events[:num_events]