from app import app

def test_get_home_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    

def test_get_books_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200

"""
This became a playwright end to end test
"""
# def test_get_books_returns_all_books():
#     client = app.test_client()
#     response = client.get("/books")
#     assert response.json == None

def test_get_films_200():
    client = app.test_client()
    response = client.get("/films")
    assert response.status_code == 200

def test_get_authors_200_all_authors():
    client = app.test_client()
    response = client.get('/authors')
    assert response.status_code == 200

def test_get_authors_all_authors():
    client = app.test_client()
    response = client.get('/authors')
    assert response.json == [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]
    
def test_get_quotes_200():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200
    assert response.json == [
      {"quote":"I may not have gone where I intended to go, but I think I have ended up where I needed to be."},
      {"quote": "I love deadlines. I love the whooshing noise they make as they go by."},
      {"quote":"The story so far: In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move."},
      {"quote":"I refuse to answer that question on the grounds that I don't know the answer"}
    
    ]


def test_get_signup_200():
    client = app.test_client()
    response = client.get("/signup_page")
    assert response.status_code == 200


def test_get_signup_thanks_200():
    client = app.test_client()
    response = client.get("/signup_thanks")
    assert response.status_code == 200


def test_get_signup_failed_200():
    client = app.test_client()
    response = client.get("/signup_failed")
    assert response.status_code == 200


def test_get_loginpage_200():
    client = app.test_client()
    response = client.get("/login_page")
    assert response.status_code == 200

def test_get_login_failed_200():
    client = app.test_client()
    response = client.get("/login_failed")
    assert response.status_code == 200