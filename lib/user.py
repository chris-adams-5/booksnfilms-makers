class User:
    def __init__(self, id, user_name, password) -> None:
        self.id = id
        self.user_name = user_name
        self.password = password

    def __repr__(self) -> str:
        return  f'User({self.id},{self.user_name},{self.password})'
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        