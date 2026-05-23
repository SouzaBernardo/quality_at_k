
class Hotel: 
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
        """
        if self.available_rooms[room_type] <= room_number:
            return False
        if not self.booked_rooms[room_type][room_number]:
            self.booked_rooms[room_type][room_number] = {name: 1}
        else:
            if self.available_rooms[room_type] > room_number:
                return False
            else:
                if self.check_in(room_type, room_number, name) and self.check_out(room_type, room_number):
                    if not self.get_available_rooms(room_type):
                        return False
                    else:
                        if self.get_available_rooms(room_type)[room_type] <= room_number:
                            return False
                        else:
                            if not self.book_room(room_type, room_number, name):
                                return False
                            else:
                                return True
        return True

    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        """
        if room_type not in self.booked_rooms[name]:
            self.booked_rooms[name] = {room_number: self.available_rooms[room_type][room_number]}
        else:
            if room_number in self.booked_rooms[name]:
                self.booked_rooms[name][room_number] += self.available_rooms[room_type][room_number]
            else:
                self.booked_rooms[name][room_number] = self.available_rooms[room_type][room_number]
        
        if room_number < self.booked_rooms[name][room_number]:
            self.booked_rooms[name][room_number] -= self.available_rooms[room_type][room_number]
        
        return True

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        """
        if room_type =='single':
            self.available_rooms['single'] += room_number
        elif room_type == 'double':
            self.available_rooms['double'] += room_number
        elif room_type == 'triple':
            self.available_rooms['triple'] += room_number


    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        
        >>> hotel.book_room('single', 1, 'guest 1')
        
        >>> hotel.get_available_rooms('double')
        3
        
        >>> hotel.book_room('double', 2, 'guest 2')
        
        >>> hotel.get_available_rooms('single')
        2
        """
        available_rooms = self.available_rooms[room_type]
        if available_rooms:
            return available_rooms
        else:
            return 0