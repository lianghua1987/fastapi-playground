from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Computer Science Pro1", "Eminem", "Keep it real", 5),
    Book(2, "How to sleep", "Eminem", "Keep it real", 3),
    Book(3, "Cook with Ann", "Ann Glidden", "Keep it real", 4),
    Book(4, "HP1", "Eminem", "Keep it real", 5),
    Book(5, "HP2", "Eminem", "Keep it real", 2)
]


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=200)
    rating: int = Field(gt=-1, lt=6)


@app.get("/books")
async def all_books():
    return BOOKS


@app.get("/books/{title}")
async def books_by_title(title: str):
    return [book for book in BOOKS if book.title == title]


@app.get("/books/")
async def books_by_title(title: str):
    return [book for book in BOOKS if book.title == title.casefold()]


def find_max_id():
    return 1 if len(BOOKS) == 0 else BOOKS[-1].id


@app.post("/books/create")
async def add_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = find_max_id() + 1
    BOOKS.append(new_book)
    return BOOKS


@app.put("/books/update")
async def update_book(book_request: BookRequest):
    updated_book = Book(**book_request.model_dump())
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == updated_book.title.casefold():
            BOOKS[i] = updated_book
    return BOOKS


@app.delete("/books/delete/{title}")
async def add_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == title.casefold():
            BOOKS.pop(i)
    return BOOKS
