class User():
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.password})"