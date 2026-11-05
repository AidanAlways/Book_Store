CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS films (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  director VARCHAR(255),
  release_year VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

TRUNCATE TABLE books, users, films RESTART IDENTITY;

INSERT INTO books (title, author) VALUES
  ('The Gruffalo', 'Julia Donaldson'),
  ('Ada Twist, Scientist', 'Andrea Beaty'),
  ('The Girl Who Drank the Moon', 'Kelly Barnhill'),
  ('Dragons in a Bag', 'Zetta Elliott'),
  ('Poor Things', 'Alasdaor Gray'),
  ('The Wind-Up Bird Chronicle', 'Haruki Murakami'),
  ('1Q84', 'Haruki Murakami');

  INSERT INTO films (title, director, release_year) VALUES
  ('Alien', 'Ridley Scott', 1979),
  ('Blade Runner', 'Ridley Scott', 1982),
  ('Lost in Translation', 'Sofia Coppola', 2003),
  ('Clayface', 'James Watkins', 2026),
  ('American Psycho', 'Mary Harron', 2000),
  ('King Kong', 'Peter Jackson', 2005),
  ('La La Land', 'Damien Chazelle', 2017);