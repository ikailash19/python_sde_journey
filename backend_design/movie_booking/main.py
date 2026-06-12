from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException

from booking_service import Booking_Service
from movie_services import Movie_Services
from movie import Movie
from seat import Seat

app = FastAPI()
movies = []

#picture1 = Movie("Titanic", 5)
#picture2 = Movie("Back to the future", 10)
#movies.append(picture1)
#movies.append(picture2)

booking_service = Booking_Service()
movie_service = Movie_Services()

@app.get("/create_movie/{movie_name}/{total_seats}")
def create_movie(movie_name, total_seats:int):
    status = movie_service.create_movie(movie_name, total_seats)
    return "Movie added successfully" if status else "Failed to create movie"

@app.get("/get_movie/{movie_id}")
def get_movie(movie_id:int):
    movie = movie_service.get_movie(movie_id)
    return "Movie ID not found" if movie == None else movie

@app.get("/all_movies")
def get_all_movies():
    return movie_service.get_all_movies()

@app.get("/book-seat/{seat_number}")
def book_seat(seat_number:int):
    movie = movie_service.get_movie(1)
    booking = booking_service.book_seat(movie, seat_number)
    return "FAILED" if not booking else booking.status

@app.get("/movies")
def get_movies():
    return {"Running movies" :[movie.movie_name for movie in movie_service.get_all_movies()]}

@app.get("/seats/{movie_id}")
def get_seats(movie_id:int):
    movie = movie_service.get_movie(movie_id)
    return {"available_seats": booking_service.show_available_seats(movie)}

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

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("/Users/kailash/PycharmProjects/python_sde_journey/backend_design/movie_booking/favicon.ico")