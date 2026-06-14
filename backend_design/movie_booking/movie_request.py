from pydantic import BaseModel

class MovieRequest(BaseModel):
    movie_name : str
    total_seats : int