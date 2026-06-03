from seat import Seat
from movie import Movie

class Booking_Service:

    def book_seat(self, movie, seat):
        for spot in movie.seats:
            if spot.seat_number == seat and not spot.is_booked:
                spot.is_booked = True
                print(f"Seat Booked for {spot.seat_number}")
                return
        print(f"{seat} seat is not available")

    def show_available_seats(self, movie):
        available_seats = []
        for seat in movie.seats:
            if not seat.is_booked:
                available_seats.append(seat.seat_number)
        return available_seats