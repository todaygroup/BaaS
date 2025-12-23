# 도메인 모델링 (Domain Modeling)

## 4.1 핵심 엔티티 정의

### 4.1.1 Author / Workspace / Project
```python
from pydantic import BaseModel, Field
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
```

### 4.1.2 Book / Part / Chapter 구조
```python
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
    part_id: Optional[str]
    order: int
    title: str
    purpose: str
    status: Literal["planned", "researching", "drafted", "revising", "final"] = "planned"
```

### 4.1.3 에이전트 실행·평가 도메인
```python
class GraphRun(BaseModel):
    id: str
    project_id: str
    book_id: Optional[str]
    graph_type: Literal["book", "chapter", "eval"]
    status: Literal["pending", "running", "succeeded", "failed"]
    started_at: datetime
    finished_at: Optional[datetime] = None

class NodeRun(BaseModel):
    id: str
    graph_run_id: str
    node_id: str
    agent_role: str
    status: Literal["pending", "running", "succeeded", "failed"]
    input_tokens: int
    output_tokens: int
    latency_ms: int
    rag_docs_used: List[str]
    error_message: Optional[str] = None
```
