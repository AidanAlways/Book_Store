FROM python:3.13
ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgres:password@book_store_db"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

