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
        
        self.movies.append({'name': name, 'price': price, 'start_time': datetime.strptime(start_time, '%H:%M'), 'end_time': datetime.strptime(end_time, '%H:%M'), 'seats': np.zeros((n, n))})



    def book_ticket(self, name, time):


    def book_ticket(self, name, seats_to_book):


    def available_movies(self, start_time, end_time):