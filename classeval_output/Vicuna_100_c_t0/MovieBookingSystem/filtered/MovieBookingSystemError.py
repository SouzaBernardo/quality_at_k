class MovieBookingSystem:
    def __init__(self):
        self.movies = []
        self.seats = np.zeros((3, 3))

    def add_movie(self, name, price, start_time, end_time, n):
        self.movies.append({'name': name, 'price': price, 'start_time': start_time, 'end_time': end_time, 'n': n})

    def book_ticket(self, name, seats_to_book):
        for i in range(len(seats_to_book)):
            row, col = seats_to_book[i]
            if self.seats[row][col] > 0:
                self.seats[row][col] -= 1
                if self.seats[row][col] == 0:
                    self.movies[self.movies.index(