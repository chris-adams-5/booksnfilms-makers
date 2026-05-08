
class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        films = []
        for film in rows:
            film_i = f"Title: {film['title']} --- Runtime: {film['run_time_minutes']} --- director:{film['director']} --- imdb: {film['imdb']}"
            films.append(film_i)
            
        return films