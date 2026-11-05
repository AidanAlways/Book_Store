from film import Film


class FilmRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM films ORDER BY id")
        return [Film(row["title"], row["director"], row["release_year"], row["id"]) for row in rows]

    def create_film(self, film):
        self._connection.execute("INSERT INTO films (title, director, release_year) VALUES (%s, %s, %s)", [film.title, film.director, film.release_year])