class Hotel:  
    """
    This is a class as hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        >>> hotel.name
        'peace hotel'
        >>> hotel.available_rooms
        available_rooms = {'single': 5, 'double': 3}
        >>> hotel.booked_rooms
        {'single': {'guest 1': 2, 'guest 2':1}, 'double': {'guest1': 1}}
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}



    def book_room(self, room_type, room_number, name):
        if room_type not in self.available_rooms:
            return False
        if room_number > self.available_rooms[room_type]:
            if self.available_rooms[room_type] == 0:
                return False
            else:
                return self.available_rooms[room_type]
        else:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            if name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] = 0
            self.booked_rooms[room_type][name] += room_number
            self.available_rooms[room_type] -= room_number
            return 'Success!'
    

    def check_in(self, room_type, room_number, name):
        if room_type not in self.booked_rooms:
            return False
        if room_number > self.booked_rooms[room_type].get(name, 0):
            return False
        if room_number == self.booked_rooms[room_type].get(name, 0):
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number
        return None
    

    def check_out(self, room_type, room_number):
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = room_number
        else:
            self.available_rooms[room_type] += room_number
    

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        return self.available_rooms[room_type]