from movie import Movie

class Movie_Services:

    def __init__(self):
        self.movies = {}
        self.next_movie_id = 1

    def create_movie(self, movie_name, total_seats):
        movie = Movie(self.next_movie_id, movie_name, total_seats)
        self.movies[self.next_movie_id] = movie
        self.next_movie_id += 1
        return True

    def get_movie(self, movie_id):
        return self.movies.get(movie_id)

    def get_all_movies(self):
        print(list(self.movies.values()))
        return list(self.movies.values())