from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title1", "author": "Author1", "category": "category1"},
    {"title": "Title2", "author": "Author2", "category": "category2"},
    {"title": "Title3", "author": "Author3", "category": "category3"},
    {"title": "Title4", "author": "Author4", "category": "category4"},
    {"title": "Title5", "author": "Author5", "category": "category2"}
]


@app.get("/books")
async def all_books():
    return BOOKS


@app.get("/books/{title}")
async def books_by_title(title: str):
    return [book for book in BOOKS if book["title"] == title]


@app.get("/books/")
async def books_by_category(category: str):
    print("here")
    return [book for book in BOOKS if book["category"].casefold() == category.casefold()]


@app.post("/books/create")
async def add_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


@app.put("/books/update")
async def add_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
    return BOOKS


@app.put("/books/delete/{title}")
async def add_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == title.casefold():
            BOOKS.pop(i)
    return BOOKS
