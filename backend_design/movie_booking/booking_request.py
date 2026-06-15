from pydantic import BaseModel

class BookingRequest(BaseModel):
    movie_id:int
    seat_number:int