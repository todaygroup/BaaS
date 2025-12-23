from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

class Author(BaseModel):
    id: str
    name: str
    email: str
    locale: str = "ko-KR"
    time_zone: str = "Asia/Seoul"

class Workspace(BaseModel):
    id: str
    name: str
    owner_id: str
    members: List[str]
    created_at: datetime

class Project(BaseModel):
    id: str
    workspace_id: str
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"
    created_at: datetime
