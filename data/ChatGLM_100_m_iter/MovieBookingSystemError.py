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
        self.movies.append({
            'name': name,
            'price': price,
           'start_time': start_time,
            'end_time': end_time,
           'seats': np.array(n)
        })

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2),...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        if name in self.movies:
            self.movies[name]['seats'] = np.array(seats_to_book)
        else:
            self.movies[name]['seats'] = np.array([seats_to_book])
        return f"Booking successful. {name} seat(s) are now in {self.movies[name]['seats']}"

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")
        start_time = start.strftime("%H:%M")
        end_time = end.strftime("%H:%M")
        movies = self.movies
        available_movies = []
        for movie in movies:
            if start_time <= movie['start_time'] <= end_time:
                available_movies.append(movie['name'])
        return available_movies