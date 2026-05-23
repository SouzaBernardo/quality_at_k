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
            if room_number <= len(self.available_rooms[room_type]):
                self.booked_rooms[room_type][room_number] = name
                self.available_rooms[room_type] -= room_number
                return "Success!"
            else:
                return len(self.available_rooms[room_type])
        else:
            return False

    def check_in(self, room_type, room_number, name):
        if room_type in self.booked_rooms and room_number > self.booked_rooms[room_type]['quantity']:
            self.booked_rooms[room_type]['quantity'] -= room_number
            self.booked_rooms[room_type]['name'].remove(name)
        else:
            return False
        self.available_rooms[room_type] -= 1
        self.available_rooms[room_type] = max(self.available_rooms[room_type], 0)
        self.booked_rooms[room_type]['quantity'] += 1
        self.booked_rooms[room_type]['name'].append(name)

    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] -= 1
        else:
            self.available_rooms[room_type] = 1
        del self.booked_rooms[room_type][room_number]

    def get_available_rooms(self, room_type):
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return 0