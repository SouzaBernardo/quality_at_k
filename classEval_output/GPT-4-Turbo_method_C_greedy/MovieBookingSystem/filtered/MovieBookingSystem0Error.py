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
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n))
        self.movies.append({'name': name, 'price': price, 'start_time': start_time, 'end_time': end_time, 'seats': seats})
    def book_ticket(self, name, seats_to_book):
        # Find the movie
        for movie in self.movies:
            if movie['name'] == name:
                # Check if all seats are available
                for seat in seats_to_book:
                    if movie['seats'][seat[0]][seat[1]] != 0:
                        return 'Booking failed.'
                # Book the seats
                for seat in seats_to_book:
                    movie['seats'][seat[0]][seat[1]] = 1
                return 'Booking success.'
        return 'Movie not found.'
    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
    
        available_movies = []
        for movie in self.movies:
            movie_start_time = movie['start_time'].time()
            movie_end_time = movie['end_time'].time()
    
            if start_time <= movie_start_time and end_time >= movie_end_time:
                available_movies.append(movie['name'])
    
        return available_movies