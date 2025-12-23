# 노드 기본 (Node Basics)

## 5.1 노드 타입
- **Trigger**: 이벤트 기반 수신.
- **Action**: LLM/RAG/Tool 호출.
- **Control Logic**: IF/Merge/Loop 제어.
- **Subgraph**: 챕터 서브그래프 호출.

## 5.2 LangGraph 노드 구현 패턴
```python
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from datetime import datetime

class BookState(TypedDict, total=False):
    topic: str
    audience: str
    tone: str
    outline: dict
    chapters_planned: List[str]
    created_at: str

def plan_outline(state: BookState) -> BookState:
    # LLM 호출 및 아웃라인 생성 로직
    # ...
    return {
        **state,
        "outline": outline_data,
        "chapters_planned": chapters,
        "created_at": datetime.utcnow().isoformat()
    }
```
