from seat import Seat
class Movie:

    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.seats = []
        for seat in range (1, total_seats+1):
            self.seats.append(Seat(seat))

