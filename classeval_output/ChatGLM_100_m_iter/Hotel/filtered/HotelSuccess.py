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
        if room_type in self.available_rooms and self.available_rooms[room_type] >= room_number:
            self.available_rooms[room_type] -= room_number
            if self.available_rooms[room_type] < 0:
                self.available_rooms[room_type] = 0
            if self.booked_rooms[name] and self.available_rooms[room_type] >= self.booked_rooms[name][0]:
                self.booked_rooms[name][0] -= room_number
                if self.booked_rooms[name][0] < 0:
                    self.booked_rooms[name][0] = 0
                if self.booked_rooms[name][0] == 0:
                    return f'Success! {name}'
        else:
            return False

    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        """
        if room_type in self.available_rooms:
            if self.available_rooms[room_type] >= self.booked_rooms[name][0]:
                self.booked_rooms[name][0] -= room_number
                if self.booked_rooms[name][0] < 0:
                    self.booked_rooms[name][0] = 0
                if self.booked_rooms[name][0] == 0:
                    return False
        else:
            return False

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        :return: True if check out successful, False otherwise
        """
        if room_type in self.available_rooms:
            if self.available_rooms[room_type] >= self.booked_rooms[name][0]:
                self.booked_rooms[name][0] -= room_number
                if self.booked_rooms[name][0] < 0:
                    self.booked_rooms[name][0] = 0
                if self.booked_rooms[name][0] == 0:
                    return False
        else:
            return False