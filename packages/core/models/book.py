from pydantic import BaseModel
from typing import List, Optional

class Chapter(BaseModel):
    id: str
    title: str
    content: Optional[str] = None
    status: str # 'draft', 'review', 'completed'

class Book(BaseModel):
    id: str
    title: str
    author: str
    outline: List[Chapter]
