from booking_service import Booking_Service
from movie import Movie
from seat import Seat

picture1 = Movie("Titanic", [Seat(1), Seat(2)])
picture2 = Movie("Back to the future", [Seat(1), Seat(2), Seat(3)])

agent = Booking_Service()
agent.book_seat(picture1, 2)
agent.book_seat(picture1, 2)
print(agent.show_available_seats(picture1))
print(agent.show_available_seats(picture2))