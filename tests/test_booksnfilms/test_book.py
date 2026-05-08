from lib.book import Book

"""
Book class inst with
id, title, author name, blurb
"""

def test_book_init():
    book = Book(1,'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")
    assert book.id == 1
    assert book.title == 'The Hitchhikers Guide to the Galaxy'
    assert book.author_name == "Douglas Adams"
    assert book.blurb == "A story that begins with a man"
    assert book.url == "url"

"""
Book
the repr method of book has been set to a
suitable str
"""

def test_book_repr():
    book = Book(1,'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")
    assert str(book) == "Book(1, The Hitchhikers Guide to the Galaxy, Douglas Adams, A story that begins with a man, url)"


"""
Book
eq method set so properties of
Book are checked as opposed to the object
makes testing easier
"""

def test_book_eq():
    book_1 = Book(1,'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")
    book_2 = Book(1,'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")

    assert book_1 == book_2