class Hotel:
    def __init__(self, name, rooms):
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
            else:
                return self.available_rooms[room_type]
        else:
            return False

    def check_in(self, room_type, room_number, name):
        if room_type in self.booked_rooms:
            if name in self.booked_rooms[room_type] and self.booked_rooms[room_type][name] >= room_number:
                self.booked_rooms[room_type][name] -= room_number
                if self.booked_rooms[room_type][name] == 0:
                    del self.booked_rooms[room_type][name]
                return True
            else:
                return False
        else:
            return False

    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return 0