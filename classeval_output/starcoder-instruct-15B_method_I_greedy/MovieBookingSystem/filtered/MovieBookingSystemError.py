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
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9,'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
       'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        movie = {
            'name': name,
            'price': price,
           'start_time': start_time,
            'end_time': end_time,
           'seats': np.zeros((n, n))
        }
        self.movies.append(movie)


    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for seat in seats_to_book:
                    if movie['seats'][seat[0], seat[1]]!= 0:
                        return 'Booking failed.'
                movie['seats'][seats_to_book[0][0], seats_to_book[0][1]] = 1
                return 'Booking success.'
        return 'Movie not found.'


    def available_movies(self, start_time, end_time):
        start_time = datetime.datetime.strptime(start_time, '%H:%M')
        end_time = datetime.datetime.strptime(end_time, '%H:%M')
        available_movies = []
        for movie in self.movies:
            if movie['start_time'] <= start_time <= movie['end_time'] or movie['start_time'] <= end_time <= movie['end_time']:
                available_movies.append(movie['name'])
        return available_movies