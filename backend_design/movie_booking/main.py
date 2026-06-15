from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException

from movie_request import MovieRequest
from booking_request import BookingRequest
from booking_service import Booking_Service
from movie_services import Movie_Services
from movie import Movie
from seat import Seat

app = FastAPI()
movies = []

booking_service = Booking_Service()
movie_service = Movie_Services()

##################/HOMEPAGE/###########################################################
@app.get("/")
def homepage():
    return "Welcome to Movie ticket booking"
######################################################################################

###################/Pydantic/#########################################################
@app.post("/movies")
def create_movie(movie_request: MovieRequest):
    movie = movie_service.create_movie(
        movie_request.movie_name,
        movie_request.total_seats
    )
    return movie
######################################################################################

###################/MOVIE/############################################################
@app.get("/add_movie/{movie_name}/{total_seats}")
def create_movie(movie_name, total_seats:int):
    status = movie_service.create_movie(movie_name, total_seats)
    return "Movie added successfully" if status else "Failed to create movie"

@app.get("/movies/{movie_id}")
def get_movie(movie_id:int):
    movie = movie_service.get_movie(movie_id)
    if movie == None:
        raise HTTPException(
            status_code = 404,
            detail = "Movie ID not found"
        )
    else:
        return movie

@app.get("/movies")
def get_all_movies():
    movies = movie_service.get_all_movies()
    if movies == []:
        raise HTTPException(
            status_code = 404,
            detail = "Movies not added"
        )
    return movies
#########################################################################################

#####################/SEAT/##############################################################
@app.get("/{movie_id}/seats")
def get_seats(movie_id:int):
    movie = movie_service.get_movie(movie_id)
    if movie == None:
        raise HTTPException(
            status_code = 404,
            detail = "Movie not found"
        )
    else:
        seats = booking_service.show_available_seats(movie)
        return {"Available_seats": seats}
###########################################################################################

#####################/PYDANTIC - BOOKINGS/#################################################
@app.post("/bookings")
def book_seat(booking_request:BookingRequest):
    movie = movie_service.get_movie(
        booking_request.movie_id
    )
    if movie == None:
        raise HTTPException(
            status_code = 404,
            detail = "Movie not found"
        )
    booking = booking_service.book_seat(
        movie,
        booking_request.seat_number
    )
    if booking == None:
        raise HTTPException(
            status_code = 404,
            detail = "Seat not found"
        )
    elif booking == False:
        raise HTTPException(
            status_code = 409,
            detail = "Seat already booked"
        )
    return booking
###########################################################################################


#####################/BOOKINGS/############################################################
@app.get("/book-seat/{movie_id}/{seat_number}")
def book_seat(movie_id:int,seat_number:int):
    movie = movie_service.get_movie(movie_id)
    booking = booking_service.book_seat(movie, seat_number)
    return "FAILED" if not booking else booking.status

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
    bookings = booking_service.get_all_bookings()
    if bookings == []:
        raise HTTPException(
            status_code = 404,
            detail = "Bookings not found"
        )
    return bookings

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
###########################################################################################

#####################\MISC\################################################################
@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("/Users/kailash/PycharmProjects/python_sde_journey/backend_design/movie_booking/favicon.ico")
###########################################################################################
