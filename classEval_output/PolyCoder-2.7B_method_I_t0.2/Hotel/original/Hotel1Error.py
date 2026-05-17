
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
        """
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :param room_type: str
        :param room_number: int, the expected number of specified type rooms to be booked
        :param name: str, guest name
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 5, 'guest 1')
        4
        >>> hotel.book_room('single', 4, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 1, 'guest 1')
        False
        >>> hotel.book_room('triple', 1, 'guest 1')
        False
        """
        if room_type not in self.available_rooms:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
            self.booked_rooms[room_type][room_number] = {'guest 1': room_number, 'guest 2': room_number}
        if room_number not in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][room_number] = {'guest 1': room_number, 'guest 2': room_number}
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_number not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_type not in self.booked_rooms[room_type][room_number]:
            return 'Not enough rooms to book'
        if room_





