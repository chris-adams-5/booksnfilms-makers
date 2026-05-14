from lib.film import Film

"""
Film class inst with
id, title, runtime mins, director, imdb
"""

def test_film_init():
    film = Film(1,'Jurassic Park', 122, 'Steven Spielberg', 'https://www.imdb.com/title/tt0107290/')
    assert film.id == 1
    assert film.title == 'Jurassic Park'
    assert film.run_time_mins == 122
    assert film.director == "Steven Spielberg"
    assert film.imdb == "https://www.imdb.com/title/tt0107290/"

"""
Film
the repr method of book has been set to a
suitable str
"""

def test_film_repr():
    book = Film(1,'Jurassic Park', 122, 'Steven Spielberg', 'https://www.imdb.com/title/tt0107290/')
    assert str(book) == "Film(1, Jurassic Park, 122, Steven Spielberg, https://www.imdb.com/title/tt0107290/)"


"""
Film
eq method set so properties of
Film are checked as opposed to the object
makes testing easier
"""

def test_film_eq():
    film_1 = Film(1,'Jurassic Park', 122, 'Steven Spielberg', 'https://www.imdb.com/title/tt0107290/')
    film_2 = Film(1,'Jurassic Park', 122, 'Steven Spielberg', 'https://www.imdb.com/title/tt0107290/')

    assert film_1 == film_2