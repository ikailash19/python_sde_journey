class Seat:

    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def book_seat(self):
        self.is_booked = True

    def unbook_seat(self):
        self.is_booked = False