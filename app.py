from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from book_repository import BookRepository
from film_repository import FilmRepository
from book import Book
from user import User
from film import Film
from user_repository import UserRepository
from authenticated import is_authenticated
from login_required import login_required

app = Flask(__name__)
app.secret_key = "some_really_secret_key"


def get_connection():
    connection = DatabaseConnection()
    connection.connect()
    return connection


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello there!."


# Books

@app.route("/books", methods=["GET"])
def get_all_books():
    book_repository = BookRepository(get_connection())
    return render_template("books.html", books=book_repository.all())


@app.route("/books", methods=["POST"])
@login_required
def create_book():
    # if "user_id" not in session:
    #     return redirect("/sessions/new")
    # connection = DatabaseConnection()
    book_repository = BookRepository(get_connection())
    details = request.form
    book_repository.create(Book(title=details["title"], author=details["author"]))
    return redirect("/books")

# Films

@app.route("/films", methods=["GET"])
def get_all_films():
    film_repository = FilmRepository(get_connection())
    return render_template("films.html", films=film_repository.all())

@app.route("/films", methods=["POST"])
def create_a_new_film():
    film_repository = FilmRepository(get_connection())
    film_details = request.form
    film = Film(title=film_details["title"], director=film_details["director"], release_year=film_details["release_year"])
    film_repository.create_film(film)
    return redirect("/films")


# Users

@app.route("/users/new", methods=["GET"])
def get_signup_form():
    return render_template("signup_form.html")


@app.route("/users", methods=["POST"])
def create_user():
    user_repository = UserRepository(get_connection())
    details = request.form
    user_repository.save(User(username=details["username"], password=details["password"]))
    return redirect("/books")

@app.route("/sessions/new", methods=["GET"])
def get_login_form():
    return render_template("login_form.html")

@app.route("/sessions", methods=["POST"])
def create_session():
    user_repository = UserRepository(get_connection())
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

# Misc

@app.route("/authors", methods=["GET"])
def get_authors():
    return [
        {"name": "Julia Donaldson", "dob": "1948-09-16"},
        {"name": "Andrea Beaty", "dob": "1961-10-08"},
        {"name": "Kelly Barnhill", "dob": "1973-01-01"},
        {"name": "Zetta Elliott", "dob": "1979-11-11"},
    ]


@app.route("/team", methods=["GET"])
def get_team():
    team = ["Aidan", "Aidan's eyes", "Aidan's hands", "Aidan's socks"]
    return render_template("team.html", team=team)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)