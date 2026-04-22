class Booking:
    def __init__(self, booking_id, seat_id):
        self.booking_id = booking_id
        self.seat_id = seat_id

    def __str__(self):
        return f"Booking(id={self.booking_id}, seat={self.seat_id})"