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
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n))
        movie = {'name': name, 'price': price, 'start_time': start_time, 'end_time': end_time, 'seats': seats}
        self.movies.append(movie)
    

    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for seat in seats_to_book:
                    row, col = seat
                    if movie['seats'][row][col] == 0:
                        movie['seats'][row][col] = 1
                    else:
                        return 'Booking failed.'
                return 'Booking success.'
        return 'Movie not found.'
    

    def available_movies(self, start_time, end_time):
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        available_movies = []
        for movie in self.movies:
            movie_start_time = datetime.strptime(movie['start_time'], '%H:%M')
            movie_end_time = datetime.strptime(movie['end_time'], '%H:%M')
            if movie_start_time >= start_time and movie_end_time <= end_time:
                available_movies.append(movie['name'])
        return available_movies
    