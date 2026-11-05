from user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def save(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [user.username, user.password])
        return None

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["username"], row["password"], row["id"])
            users.append(item)
        return users

    def find_by_username(self, username):
        user_details = self._connection.execute(
            'SELECT * FROM users WHERE username = %s', [username]
        )[0]

        return User(
            user_details["username"],
            user_details["password"],
            user_details["id"]
        )