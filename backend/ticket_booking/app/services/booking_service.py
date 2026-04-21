from app.models.booking import Booking

class BookingService:
    def __init__(self):
        self.bookings = []

    def book_seat(self, show, seat_id):
        seat = show.seats[seat_id]

        if seat.is_booked:
            return "Seat already booked"

        seat.is_booked = True
        booking = Booking(len(self.bookings), seat_id)
        self.bookings.append(booking)

        return booking
