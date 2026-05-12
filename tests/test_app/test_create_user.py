

from app import app

def test_create_user_is_saved_to_database(db_connection):
    # create the test client to send requests without using Playwright and a browser
    db_connection.seed('seedsgit add t/booksnfilms.pgsql')
    client = app.test_client()

   # send the request
    response = client.post('/signup', data={
        'user_name': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'

    

