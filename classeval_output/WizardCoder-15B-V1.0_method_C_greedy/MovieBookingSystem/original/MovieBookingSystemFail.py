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
        movie = {'name': name, 'price': price,'start_time': start_time, 'end_time': end_time,'seats': seats}
        self.movies.append(movie)


    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2),...]
        :return: str, booking status message. "Movie not found." for no such movie.
                 "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                seats = movie['seats']
                for seat in seats_to_book:
                    if seats[seat[0]][seat[1]] == 0:
                        seats[seat[0]][seat[1]] = 1
                    else:
                        return "Booking failed."
                movie['seats'] = seats
                return "Booking success."
        return "Movie not found."

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = datetime.strptime(end_time, '%H:%M').time()
        available_movies = []
        for movie in self.movies:
            if movie['start_time'] <= start_time <= movie['end_time'] or movie['start_time'] <= end_time <= movie['end_time']:
                available_movies.append(movie['name'])
        return available_movies