from datetime import datetime, timedelta
class CalendarUtil: 
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        self.events = []



    def add_event(self, event):
        """
        :param event: The event to be added to the calendar, dict.
        """
        self.events.append(event)
    

    def remove_event(self, event):
        """
        :param event: The event to be removed from the calendar, dict.
        """
        self.events.remove(event)
    

    def get_events(self, date):
        """
        :param date: The date to get events for, datetime.
        :return: A list of events on the given date, list.
        """
        events_on_date = []
        for event in self.events:
            if event['date'].date() == date.date():
                events_on_date.append(event)
        return events_on_date
    

    def is_available(self, start_time, end_time):
        """
        :param start_time: The start time of the time slot, datetime.
        :param end_time: The end time of the time slot, datetime.
        :return: True if the calendar is available for the given time slot, False otherwise, bool.
        """
        for event in self.events:
            if start_time < event['end_time'] and end_time > event['start_time']:
                return False
        return True
    

    def get_available_slots(self, date):
        available_slots = []
        previous_end_time = datetime.combine(date, datetime.min.time())
    
        for event in self.events:
            if event['date'] == date:
                start_time = event['start_time']
                end_time = event['end_time']
    
                if start_time > previous_end_time:
                    available_slots.append((previous_end_time, start_time))
    
                previous_end_time = end_time
    
        return available_slots
    

    def get_upcoming_events(self, num_events):
        upcoming_events = []
        sorted_events = sorted(self.events, key=lambda event: event['date'])
        for event in sorted_events:
            if len(upcoming_events) < num_events:
                upcoming_events.append(event)
            else:
                break
        return upcoming_events