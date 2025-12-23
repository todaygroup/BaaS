from pydantic import BaseModel
from typing import List, Literal, Dict, Any

Level = Literal["concept", "framework", "case", "data"]

class ChunkMetadata(BaseModel):
    source: str           # filename or URL
    page: int
    section: Optional[str] = None
    topics: List[str] = []
    level: Level = "concept"
    part_candidates: List[int] = []
    language: str = "ko"
    created_at: str
