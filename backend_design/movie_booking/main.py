from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException

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
    booking = booking_service.book_seat(picture1, seat_number)
    return "FAILED" if not booking else booking.status

@app.get("/movies")
def get_movies():
    return {"Running movies" :[movie.movie_name for movie in movies]}

@app.get("/seats")
def get_seats():
    return {"available_seats": booking_service.show_available_seats(picture1)}

@app.get("/bookings/{booking_id}")
def get_booking(booking_id:int):
    booking = booking_service.get_booking(booking_id)
    if booking is None:
        raise HTTPException(
            status_code = 404,
            detail = "Booking not found"
        )
    return booking

@app.get("/bookings")
def get_all_bookings():
    return booking_service.get_all_bookings()

@app.get("/cancel/{booking_id}")
def cancel_booking(booking_id:int):
    status = booking_service.cancel_booking(booking_id)
    if not status:
        raise HTTPException(
            status_code = 400,
            detail = "Booking not found or already cancelled"
        )
    else:
        return "Booking cancelled!"

@app.get("/")
def homepage():
    return "Welcome to Movie ticket booking"
print(booking_service.show_available_seats(picture2))

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("/Users/kailash/PycharmProjects/python_sde_journey/backend_design/movie_booking/favicon.ico")