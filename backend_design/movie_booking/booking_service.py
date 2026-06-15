from seat import Seat
from movie import Movie
from booking import Booking
from booking_status import BookingStatus
from datetime import datetime

class Booking_Service:

    def __init__(self):
        self.next_booking_id = 1
        self.bookings = {}

    def book_seat(self, movie, seat):
        spot = movie.get_seat(seat)
        #Seat not available
        if spot is None:
            return None

        if spot.is_booked:
            return False

        spot.book_seat()
        booking = Booking(self.next_booking_id, movie, spot, datetime.now(), BookingStatus.BOOKED)
        self.bookings[booking.booking_id] = booking
        self.next_booking_id += 1
        return booking

    def show_available_seats(self, movie):
        available_seats = []
        for seat in movie.get_all_seats():
            if not seat.is_booked:
                available_seats.append(seat.seat_number)
        return available_seats

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)

    def get_all_bookings(self):
        return list(self.bookings.values())

    def cancel_booking(self, booking_id):
        booking = self.bookings.get(booking_id)

        if booking is None:
            return False

        if booking.status == BookingStatus.CANCELLED:
            return False

        booking.status = BookingStatus.CANCELLED
        booking.seat.unbook_seat()

        return True