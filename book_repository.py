from book import Book


class BookRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books ORDER BY id")
        return [Book(row["title"], row["author"], row["id"]) for row in rows]

    def create(self, book):
        self._connection.execute(
            "INSERT INTO books (title, author) VALUES (%s, %s)",
            [book.title, book.author],
        )