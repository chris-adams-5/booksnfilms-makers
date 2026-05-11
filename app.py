from flask import Flask, render_template, request, redirect

from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
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


@app.route('/authors', methods=['GET'])
def get_authors():
    return authors

@app.route('/quotes', methods=['GET'])
def get_quotes():
    return quotes


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
