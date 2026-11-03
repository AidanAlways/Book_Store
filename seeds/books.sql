CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

TRUNCATE TABLE books, users RESTART IDENTITY;

INSERT INTO books (title, author) VALUES
  ('The Gruffalo', 'Julia Donaldson'),
  ('Ada Twist, Scientist', 'Andrea Beaty'),
  ('The Girl Who Drank the Moon', 'Kelly Barnhill'),
  ('Dragons in a Bag', 'Zetta Elliott'),
  ('Poor Things', 'Alasdaor Gray'),
  ('The Wind-Up Bird Chronicle', 'Haruki Murakami'),
  ('1Q84', 'Haruki Murakami');