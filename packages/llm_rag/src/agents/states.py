from typing import TypedDict, List, Optional

class BookState(TypedDict, total=False):
    book_id: str
    topic: str
    audience: str
    tone: str
    outline: dict
    parts: List[dict]
    chapters: List[dict]
    errors: List[str]

class ChapterState(TypedDict, total=False):
    chapter_id: str
    book_id: str
    part_id: Optional[str]
    title: str
    purpose: str
    outline: dict
    research_notes: List[dict]
    case_studies: List[dict]
    draft_text: str
    eval_score: float
    eval_feedback: str
    iteration: int
    errors: List[str]
    rag_citations: List[str]
