from fastapi import APIRouter, Depends
from packages.workflows.book_graph import book_graph
from packages.workflows.chapter_graph import chapter_graph

router = APIRouter(prefix="/graphs", tags=["graphs"])

@router.post("/book/run")
async def run_book_graph(book_id: str):
    # In a real app, this would start a background task
    initial_state = {"book_id": book_id}
    # result = await book_graph.ainvoke(initial_state)
    return {"status": "started", "run_id": "mock_run_id"}

@router.post("/chapter/run")
async def run_chapter_graph(chapter_id: str):
    return {"status": "started", "run_id": "mock_run_id_chapter"}
