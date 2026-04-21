from app.models.seat import Seat

class Show:
    def __init__(self, show_id, total_seats):
        self.show_id = show_id
        self.seats = [Seat(i) for i in range(total_seats)]

    def get_available_seats(self):
        return [seat for seat in self.seats if not seat.is_booked]