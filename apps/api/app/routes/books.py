from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/")
async def list_books():
    return []

@router.post("/")
async def create_book(title: str):
    return {"id": "new_book_id", "title": title}
