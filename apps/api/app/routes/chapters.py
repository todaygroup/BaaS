from fastapi import APIRouter

router = APIRouter(prefix="/chapters", tags=["chapters"])

@router.get("/{book_id}")
async def list_chapters(book_id: str):
    return []
