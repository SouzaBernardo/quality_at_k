from datetime import datetime
import numpy as np
class MovieBookingSystem:  
    """
    this is a class as movie booking system, which allows to add movies, book tickets and check the available movies within a given time range. 
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        self.movies = []



    def add_movie(self, name, price, start_time, end_time, n):
        self.movies.append({'name': name, 'price': price, 'start_time': start_time, 'end_time': end_time, 'seats': np.zeros((n, n))})

    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if name == movie['name']:
                seats_to_book = [(row, col) for row, col in seats_to_book if row in movie['seats'][0] and col in movie['seats'][1]]
                if len(seats_to_book) == len(seats_to_book[0]):
                    for row, col in seats_to_book:
                        if row in movie['seats'][0] and col in movie['seats'][1]:
                            movie['seats'][0][row][col] = 1
                            movie['seats'][1][row][col] = 1
                            return "Booking success."
                        else:
                            return "Booking failed."
                else:
                    return "Booking failed."
            else:
                return "Movie not found."