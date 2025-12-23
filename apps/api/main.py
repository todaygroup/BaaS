from fastapi import FastAPI
from packages.core.models.book import Book, Chapter

app = FastAPI(title="BAAS API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Welcome to BAAS API"}

@app.post("/books")
async def create_book(book: Book):
    return {"status": "created", "book": book}
