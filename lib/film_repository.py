from lib.film import Film


class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        films = []
        for film in rows:
            film_i = Film(film['id'],film['title'], film['run_time_minutes'], film['director'],film['imdb'])
            films.append(film_i)
            
        return films
    
    def create(self,new_film : Film):

        self._connection.execute('' \
        'INSERT INTO films (title, director, run_time_minutes, imdb) VALUES (%s, %s, %s, %s)', 
        [new_film.title, new_film.director, new_film.run_time_mins, new_film.imdb]
        )

        return None