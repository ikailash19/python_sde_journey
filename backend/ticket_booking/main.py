from app.models.show import Show
from app.services.booking_service import BookingService

show = Show(1, 5)
booking_service = BookingService()

print("Available seats:", [s.seat_id for s in show.get_available_seats()])

print(booking_service.book_seat(show, 2))
print(booking_service.book_seat(show, 2))

print("Available seats:", [s.seat_id for s in show.get_available_seats()])