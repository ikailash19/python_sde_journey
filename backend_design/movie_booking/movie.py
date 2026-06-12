from seat import Seat
class Movie:

    def __init__(self, movie_id, movie_name, total_seats):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.seats = {}
        if total_seats < 1:
            raise ValueError("Total seats must be positive")
        for seat in range (1, total_seats+1):
            self.seats[seat] = Seat(seat)

    def get_seat(self, seat_number):
        return self.seats.get(seat_number)

    def get_all_seats(self):
        return self.seats.values()