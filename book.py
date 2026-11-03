class Book:
    def __init__(self, title, author, id=None):
        self.id = id
        self.title = title
        self.author = author

    # Two books are equal if all their attributes match,
    # rather than only when they're the same object in memory.
    def __eq__(self, other):
        return isinstance(other, Book) and self.__dict__ == other.__dict__

    # Controls how a book prints, e.g. Book(1, The Gruffalo, Julia Donaldson)
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author})"