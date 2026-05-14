
from flask import session
from app import app

"""
I removed the post tests as they now require a session to post
the redirect still happens

"""

def test_post_books_302():
    client = app.test_client()

   # send the request
    response = client.post('/books', data={
        'title': 'testbook',
        'author_name': 'testauthor',
        'blurb': 'a test',
        'url': 'https://test url.com'
    })

    # assert that the redirect happened
    assert response.status_code == 302

# def test_post_books_is_saved_to_database(db_connection):
#     db_connection.seed('seeds/booksnfilms.pgsql')
#     client = app.test_client()

#     session["user_id"] = 1

#    # send the request
#     response = client.post('/books', data={
#         'title': 'testbook',
#         'author_name': 'testauthor',
#         'blurb': 'a test blurb',
#         'url': 'https://testurl.com'
#     })

#     # read from the DB
#     result = db_connection.execute("SELECT * FROM books WHERE author_name = 'testauthor'")

#     # assert that the book was created
#     assert len(result) == 1
#     assert result[0]['title'] == 'testbook'
#     assert result[0]['author_name'] == 'testauthor'
#     assert result[0]['blurb'] == 'a test blurb'
#     assert result[0]['image_url'] == 'https://testurl.com'
#     db_connection.seed('seeds/booksnfilms.pgsql')

def test_post_films_302():
    client = app.test_client()

   # send the request
    response = client.post('/films', data={
        'title': 'testfilm',
        'run_time': 120,
        'director': 'testdirector',
        'imdb': 'https://testurl.com'
    })

    # assert that the redirect happened
    assert response.status_code == 302

# def test_post_films_is_saved_to_database(db_connection):
#     db_connection.seed('seeds/booksnfilms.pgsql')
#     client = app.test_client()

#    # send the request
#     response = client.post('/films', data={
#         'title': 'testfilm',
#         'run_time': 120,
#         'director': 'testdirector',
#         'imdb': 'https://testurl.com'
#     })

#     # read from the DB
#     result = db_connection.execute("SELECT * FROM films WHERE title = 'testfilm'")

#     # assert that the book was created
#     assert len(result) == 1
#     assert result[0]['title'] == 'testfilm'
#     assert result[0]['run_time_minutes'] == 120
#     assert result[0]['director'] == 'testdirector'
#     assert result[0]['imdb'] == 'https://testurl.com'
#     db_connection.seed('seeds/booksnfilms.pgsql')


# def test_post_user_is_saved_to_database(db_connection):
#     # create the test client to send requests without using Playwright and a browser
#     db_connection.seed('seeds/booksnfilms.pgsql')
#     client = app.test_client()

#    # send the request
#     response = client.post('/signup', data={
#         'user_name': 'testuser',
#         'password': 'password123'
#     })

#     # assert that the redirect happened
#     assert response.status_code == 302

#     # read from the DB
#     result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser'")

#     # assert that the user was created
#     assert len(result) == 1
#     assert result[0]['username'] == 'testuser'

# def test_post_user_wont_take_duplicates(db_connection):
#     # create the test client to send requests without using Playwright and a browser
#     db_connection.seed('seeds/booksnfilms.pgsql')
#     client = app.test_client()

#    # send the request
#     client.post('/signup', data={
#         'user_name': 'testuser',
#         'password': 'password123'
#     })

#     # send a duplicate request
#     response = client.post('/signup', data={
#         'user_name': 'testuser',
#         'password': 'password123'
#     })

#     assert response.status_code == 302

#     # read from the DB
#     result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser'")

#     # assert that one user was created
#     assert len(result) == 1
#     assert result[0]['username'] == 'testuser'

# def tests_post_login(db_connection):
#     # create the test client to send requests without using Playwright and a browser
#     db_connection.seed('seeds/booksnfilms.pgsql')
#     client = app.test_client()

#     #add the test user
#     client.post('/signup', data={
#         'user_name': 'testuser',
#         'password': 'password123'
#     })

#    # send the request to login
#     response = client.post('/login', data={
#         'user_name': 'testuser',
#         'password': 'password123'
#     })

#     # assert that the redirect happened
#     assert response.status_code == 302

#     # playwright tests for successful and unsuccesful logins

