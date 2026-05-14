from flask import Flask, render_template, request, redirect

from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
from lib.film import Film
from lib.user_repository import UserRepository
from lib.user import User
from data.authors import authors
from data.quotes import quotes

# instantiate a Flask app object
app = Flask(__name__)


connection = DatabaseConnection()
connection.connect()

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/', methods= ["GET"])
def index():
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def get_books():
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books = books)

@app.route('/books', methods=['POST'])
def create_book():
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(None,book_details['title'], book_details['author_name'], book_details['blurb'], book_details['url'])
    book_repository.create(book)
    return redirect('/books')

@app.route('/films', methods=['GET'])
def get_films():
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films = films)

@app.route('/films', methods=['POST'])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(
        id=None,
        title=film_details['title'],
        director=film_details['director'],
        run_time_mins=film_details['run_time'],
        imdb=film_details['imdb'] 
        )
    film_repository.create(film)
    return redirect('/films')


@app.route('/authors', methods=['GET'])
def get_authors():
    return authors

@app.route('/quotes', methods=['GET'])
def get_quotes():
    return quotes

@app.route('/signup_page', methods=['GET'])
def get_signup():
    return render_template('signup_page.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    user_repository = UserRepository(connection)
    user_details = request.form
    new_user = User(None, user_details['user_name'], user_details['password'])
    is_succesful = user_repository.create(new_user)
    if is_succesful:
        return redirect('/signup_thanks')
    return redirect('/signup_failed')

@app.route('/signup_thanks', methods=['GET'])
def get_signup_thanks():
    return render_template('signup_thanks.html')

@app.route('/signup_failed', methods = ['GET'])
def get_signup_failed():
    return render_template('signup_failed.html')


@app.route('/login_page', methods=['GET'])
def get_login():
    return render_template('login_page.html')


@app.route('/login', methods=['POST'])
def post_login():
    user_repository = UserRepository(connection)
    user_details = request.form
    new_user = User(None, user_details['user_name'], user_details['password'])
    is_successful = user_repository.login(new_user)
    if is_successful:
        return redirect('/')
    return redirect('/login')

@app.route('/login_failed', methods = ['GET'])
def get_login_failed():
    return render_template('login_failed.html')

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
