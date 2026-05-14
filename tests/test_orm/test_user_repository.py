from lib.user_repository import UserRepository
from lib.user import User

"""
Call user repository all and
return a list of user objects
which reflect the seed test data
"""

def test_user_repository_all(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    users = repository.all()

    assert users == [
        User(1,'user', 'password'),
        User(2,'speckled_jim','meeeh')
    ]

"""
Create an entry for a user
"""

def test_user_repository_create(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    new_user = User(None, 'Ford Prefect', 'Mostly_Harml3ss')
    result = repository.create(new_user)
    assert result == True
    users = repository.all()
    assert users == [
        User(1,'user', 'password'),
        User(2,'speckled_jim','meeeh'),
        User(3, 'Ford Prefect', 'Mostly_Harml3ss')
    ]


"""
rejects a user if the username is already in the db
"""

def test_user_repository_create_duplicate(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    new_user = User(None, 'Ford Prefect', 'Mostly_Harml3ss')
    repository.create(new_user)
    result = repository.create(new_user)
    assert result == False
    users = repository.all()
    assert users == [
        User(1,'user', 'password'),
        User(2,'speckled_jim','meeeh'),
        User(3, 'Ford Prefect', 'Mostly_Harml3ss')
    ]

"""
Delete an entry from users
"""

def test_user_repository_delete(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    result = repository.delete(1) # I apologise to no one
    assert result == None
    users = repository.all()

    assert users == [
        User(2,'speckled_jim','meeeh')
    ]
    # I put it back in as this was the last test to run and it was causing me trouble
    db_connection.seed("seeds/booksnfilms.pgsql")


"""
find user by id
"""

def test_user_login(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    new_user = User(None, 'Ford Prefect', 'Mostly_Harml3ss')
    repository.create(new_user)
    user = repository.find_user_by_username(new_user.user_name)
    assert user == User(3, 'Ford Prefect', 'Mostly_Harml3ss')


"""
When I call find on UserRepository with an id
I get beck the corresponding user
"""

def test_user_repository_find(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2,'speckled_jim','meeeh')


