from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user import User
from user_repository import UserRepository

app = Flask(__name__)


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
def create_book():
    book_repository = BookRepository(get_connection())
    details = request.form
    book_repository.create(Book(title=details["title"], author=details["author"]))
    return redirect("/books")


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