from fastapi import APIRouter, Depends
from packages.workflows.book_graph import book_graph
from packages.workflows.chapter_graph import chapter_graph

router = APIRouter(prefix="/graphs", tags=["graphs"])

@router.post("/book/run")
async def run_book_graph(book_id: str, topic: str, audience: str, tone: str = "Professional"):
    initial_state = {
        "book_id": book_id,
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "outline": "",
        "chapters": []
    }
    # In a real app, this would be a background task (e.g., Celery, arq)
    # For now, we run it directly for the functional vertical slice
    result = await book_graph.ainvoke(initial_state)
    return {"status": "completed", "run_id": f"run_{book_id}", "result": result}

@router.post("/chapter/run")
async def run_chapter_graph(chapter_id: str):
    return {"status": "started", "run_id": "mock_run_id_chapter"}
