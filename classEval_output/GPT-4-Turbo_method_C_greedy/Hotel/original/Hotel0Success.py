
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
        if room_type in self.available_rooms:
            if self.available_rooms[room_type] >= room_number:
                self.available_rooms[room_type] -= room_number
                if room_type in self.booked_rooms:
                    if name in self.booked_rooms[room_type]:
                        self.booked_rooms[room_type][name] += room_number
                    else:
                        self.booked_rooms[room_type][name] = room_number
                else:
                    self.booked_rooms[room_type] = {name: room_number}
                return 'Success!'
            elif self.available_rooms[room_type] > 0:
                return self.available_rooms[room_type]
            else:
                return False
        else:
            return False
    
    def check_in(self, room_type, room_number, name):
        if room_type in self.booked_rooms:
            if name in self.booked_rooms[room_type]:
                if self.booked_rooms[room_type][name] >= room_number:
                    self.booked_rooms[room_type][name] -= room_number
                    if self.booked_rooms[room_type][name] == 0:
                        del self.booked_rooms[room_type][name]
                    return True
        return False
    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number
        for guest, rooms in self.booked_rooms[room_type].items():
            if rooms >= room_number:
                self.booked_rooms[room_type][guest] -= room_number
                if self.booked_rooms[room_type][guest] == 0:
                    del self.booked_rooms[room_type][guest]
                break
            else:
                room_number -= rooms
                del self.booked_rooms[room_type][guest]
    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return "Room type not found in this hotel."
