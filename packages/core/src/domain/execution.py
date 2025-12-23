from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

class GraphRun(BaseModel):
    id: str
    project_id: str
    book_id: Optional[str] = None
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
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: int = 0
    rag_docs_used: List[str] = []
    error_message: Optional[str] = None

class EvalResult(BaseModel):
    id: str
    node_run_id: str
    score_overall: float
    score_structure: float
    score_logic: float
    score_style: float
    comments: str
    created_at: datetime
