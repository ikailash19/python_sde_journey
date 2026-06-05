from seat import Seat
from movie import Movie

class Booking_Service:

    def book_seat(self, movie, seat):
        spot = movie.get_seat(seat)
        #Seat not available
        if spot is None:
            return False

        if not spot.is_booked:
            spot.book_seat()
            return True

        return False

    def show_available_seats(self, movie):
        available_seats = []
        for seat in movie.get_all_seats():
            if not seat.is_booked:
                available_seats.append(seat.seat_number)
        return available_seats