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
        self.movies.append({'name': name, 'price': price,'start_time': start_time, 'end_time': end_time, 'n': n})



    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2),...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """
        if len(seats_to_book) == 0:
            return 'Movie not found.'
        if len(seats_to_book) == 1:
            seats_to_book = [(seats_to_book[0][0], seats_to_book[0][1])]
        seats_to_book = np.array(seats_to_book)
        if seats_to_book.shape[0]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[1]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[2]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[3]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[4]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[5]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[6]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[7]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[8]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[9]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[10]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[11]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[12]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[13]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[14]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[15]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[16]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[17]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[18]!= self.movies[0]['n']:
            return 'Movie not found.'
        if seats_to_book.shape[19]!= self.movies[0]['n']:
            return 'Movie not found.'

    def available_movies(self, start_time, end_time):