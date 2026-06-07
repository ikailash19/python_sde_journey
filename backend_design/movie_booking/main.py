from fastapi import FastAPI
from booking_service import Booking_Service
from movie import Movie
from seat import Seat

app = FastAPI()
movies = []

picture1 = Movie("Titanic", 5)
picture2 = Movie("Back to the future", 10)
movies.append(picture1)
movies.append(picture2)

booking_service = Booking_Service()

@app.get("/book-seat/{seat_number}")
def book_seat(seat_number:int):
    status = booking_service.book_seat(picture1, seat_number)
    return "Seat Booked" if status else "Not Booked"

@app.get("/movies")
def get_movies():
    return {"Running movies" :[movie.movie_name for movie in movies]}

@app.get("/seats")
def get_seats():
    return {"available_seats": booking_service.show_available_seats(picture1)}

print(booking_service.show_available_seats(picture2))