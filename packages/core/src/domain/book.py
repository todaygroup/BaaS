from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

class Book(BaseModel):
    id: str
    project_id: str
    title: str
    subtitle: Optional[str] = None
    target_audience: str
    tone: str
    language: str = "ko"
    status: Literal["outline", "drafting", "editing", "completed"] = "outline"
    created_at: datetime

class Part(BaseModel):
    id: str
    book_id: str
    order: int
    title: str
    description: Optional[str] = None

class Chapter(BaseModel):
    id: str
    book_id: str
    part_id: Optional[str] = None
    order: int
    title: str
    purpose: str
    status: Literal["planned", "researching", "drafted", "revising", "final"] = "planned"
    created_at: datetime
