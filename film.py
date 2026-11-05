class Film:
    def __init__(self, title, director, release_year, id=None):
        self.id = id
        self.title = title
        self.director = director
        self.release_year = release_year

    def __eq__(self, other):
        return isinstance(other, Film) and self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Film({self.id}, {self.title}, {self.director}, {self.release_year})"