from datetime import datetime
import numpy as np
class MovieBookingSystem: 
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


    def available_movies(self, start_time, end_time):