class Booking:

    def __init__(
            self,
            booking_id,
            movie,
            seat,
            booking_time,
            status
    ):
        self.booking_id = booking_id
        self.movie = movie
        self.seat = seat
        self.booking_time = booking_time
        self.status = status