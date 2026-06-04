from booking_service import Booking_Service
from movie import Movie
from seat import Seat

picture1 = Movie("Titanic", 5)
picture2 = Movie("Back to the future", 10)

agent = Booking_Service()
status = agent.book_seat(picture1, 2)
print ("Seat Booked" if status else "Not Booked")
status = agent.book_seat(picture1, 2)
print ("Seat Booked" if status else "Not Booked")
print(agent.show_available_seats(picture1))
print(agent.show_available_seats(picture2))