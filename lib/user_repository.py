from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")

        return [User(row["id"],row["username"],row["password"]) for row in rows]
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s', [user_id]
        )
        row = rows[0]
        return User(row["id"],row["username"],row["password"])
    
    def create(self,new_user : User):
        rows = self._connection.execute("SELECT username FROM users WHERE username=%s", [new_user.user_name])
        if len(rows) == 1:
            return False
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [new_user.user_name, new_user.password])
        return True

    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None
    
    def find_user_by_username(self, user_name):
        rows = self._connection.execute('SELECT * FROM users WHERE username = %s', [user_name])
        if len(rows) != 1:
            return None
        row = rows[0]
        return User(row["id"],row["username"],row["password"])