To complete the class MovieBookingSystem, you need to implement the following methods:

1. add\_movie(self, name, price, start\_time, end\_time, n):
This method should add a new movie into the self.movies list. The movie's name, price, start\_time, end\_time, and number of seats should be passed as arguments.
2. book\_ticket(self, name, seats\_to\_book):
This method should book tickets for a movie. The movie's name and the number of seats to book should be passed as arguments. The method should change the seats value in the self.movies list if the booking is successful.
3. available\_movies(self, start\_time, end\_time):
This method should get a list of available movies within the specified time range.

You also need to add the following attributes to the class:

1. self.movies: list of dictionaries, where each dictionary represents a movie and contains the movie's name, price, start\_time, end\_time, and number of seats.
2. self.seats: array of arrays, where each array represents the number of seats available in a row and column.

You can use the following code as a starting point for implementing the above methods:
```
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
```