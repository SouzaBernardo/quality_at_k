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
        if self.available_rooms[room_type] < room_number:
            return self.available_rooms[room_type]
        self.available_rooms[room_type] -= room_number
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        self.booked_rooms[room_type][name] = room_number
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        if room_type not in self.booked_rooms:
            return False
        if room_number not in self.booked_rooms[room_type]:
            return False
        if room_number > self.booked_rooms[room_type][name]:
            self.booked_rooms[room_type][name] -= room_number
        else:
            del self.booked_rooms[room_type][name]
        return True

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.check_out('single', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3}
        >>> hotel.check_out('triple', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3, 'triple': 2}
        """
        if room_type not in self.booked_rooms:
            return False
        if room_number not in self.booked_rooms[room_type]:
            return False
        if room_number > self.booked_rooms[room_type][room_number]:
            self.booked_rooms[room_type][room_number] -= room_number
        else:
            del self.booked_rooms[room_type][room_number]
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = 0
        self.available_rooms[room_type] += room_number
        return True