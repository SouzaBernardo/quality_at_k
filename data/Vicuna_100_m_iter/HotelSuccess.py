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
        available_rooms = self.available_rooms[room_type]
        if room_number > available_rooms:
            return False
        self.booked_rooms[name] = room_type
        self.available_rooms[room_type] -= room_number
        return "Success!"

    def check_in(self, room_type, room_number, name):
        available_rooms = self.available_rooms[room_type]
        if room_number > available_rooms:
            return False
        if name in self.booked_rooms:
            if self.booked_rooms[name][room_type] == room_number:
                self.booked_rooms[name].pop(room_type, None)
                self.available_rooms[room_type] += self.booked_rooms[name][room_type]
                return "Success!"
            else:
                return False
        else:
            self.booked_rooms[name] = {'room_type': room_type, 'quantity': 1}
            self.available_rooms[room_type] -= 1
            return "Success!"

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
        if room_type in self.available_rooms:
            self.available_rooms[room_type] -= room_number
        elif room_type not in self.available_rooms:
            self.available_rooms[room_type] = {'single': 1, 'double': 1, 'triple': 1}
            self.available_rooms[room_type]['single'] -= 1
            self.available_rooms[room_type]['double'] -= 1
            self.available_rooms[room_type]['triple'] -= 1
        else:
            return "Room type not found"

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        available_rooms = self.available_rooms[room_type]
        if room_type in self.available_rooms:
            return available_rooms
        else:
            return "Room type not found"