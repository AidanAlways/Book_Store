import os
import sys

import pytest
from playwright.sync_api import Page, expect

# Lets the tests import app and database_connection from the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from app import app
from database_connection import DatabaseConnection

BASE_URL = "http://127.0.0.1:5001"
SEED_FILE = os.path.join(PROJECT_ROOT, "seeds", "books.sql")

SEEDED_TITLES = [
    "The Gruffalo",
    "Ada Twist, Scientist",
    "The Girl Who Drank the Moon",
    "Dragons in a Bag",
    "Poor Things",
    "The Wind-Up Bird Chronicle",
    "1Q84",
]

EXPECTED_AUTHORS = [
    {"name": "Julia Donaldson", "dob": "1948-09-16"},
    {"name": "Andrea Beaty", "dob": "1961-10-08"},
    {"name": "Kelly Barnhill", "dob": "1973-01-01"},
    {"name": "Zetta Elliott", "dob": "1979-11-11"},
]


@pytest.fixture(autouse=True)
def reset_database():
    """Reseed the database before every test so each one starts from known data."""
    connection = DatabaseConnection()
    connection.connect()
    connection.seed(SEED_FILE)


@pytest.fixture
def client():
    return app.test_client()


# Flask test client tests (no browser needed)

def test_get_books_returns_a_200(client):
    response = client.get("/books")
    assert response.status_code == 200


def test_get_books_returns_all_the_books(client):
    # /books returns an HTML page, so check that each title appears in the body
    html = client.get("/books").get_data(as_text=True)
    for title in SEEDED_TITLES:
        assert title in html


def test_get_authors_returns_a_200(client):
    response = client.get("/authors")
    assert response.status_code == 200


def test_get_authors_returns_all_the_authors(client):
    response = client.get("/authors")
    assert response.json == EXPECTED_AUTHORS


# Playwright tests (the server must be running on port 5001)

def test_landing_page_has_title(page: Page):
    page.goto(BASE_URL)
    expect(page.locator("h1")).to_have_text("Welcome to the book store o/")


def test_books_page_lists_all_books(page: Page):
    page.goto(f"{BASE_URL}/books")
    # the template sorts books by author
    expect(page.locator("li")).to_have_text([
        "Poor Things by Alasdaor Gray",
        "Ada Twist, Scientist by Andrea Beaty",
        "The Wind-Up Bird Chronicle by Haruki Murakami",
        "1Q84 by Haruki Murakami",
        "The Gruffalo by Julia Donaldson",
        "The Girl Who Drank the Moon by Kelly Barnhill",
        "Dragons in a Bag by Zetta Elliott",
    ])


def test_new_book_appears_in_the_list(page: Page):
    page.goto(f"{BASE_URL}/books")
    page.get_by_label("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()

    # sorted by author, "Geronimo" lands third
    expect(page.locator("li").nth(2)).to_have_text(
        "The Chronicles of Geronimo (the cat) by Geronimo"
    )