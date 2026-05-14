from lib.user import User


def test_user_init():
    user =User(1,'user','password')
    assert user.id == 1
    assert user.user_name == 'user'
    assert user.password == 'password'


def test_user__rpr__():
    user =User(1,'user','password')
    assert str(user) == 'User(1,user,password)'

def test_user__eq__():
    user1 =User(1,'user','password')
    user2 =User(1,'user','password')
    assert user1 == user2

