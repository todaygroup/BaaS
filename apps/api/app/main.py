from fastapi import FastAPI, Depends
from .config import settings
from .routes import books, chapters, graphs

app = FastAPI(title="BAAS API", version="0.1.0")

app.include_router(books.router)
app.include_router(chapters.router)
app.include_router(graphs.router)

@app.get("/")
async def root():
    return {"message": "Welcome to BAAS API", "env": settings.env}
