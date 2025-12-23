# 노드 카탈로그 (Node Catalog)

## 6.1 카테고리
- **Planning**: BookOutlinePlanner, ChapterPlanner.
- **RAG**: ResearchRetriever, RelevanceChecker.
- **Writing**: ChapterWriter, StyleLocalizer.
- **Evaluation**: AutoCriticAgent.
- **Utility**: AggregateChapters, Exporter.

## 6.2 노드 스키마
```python
from pydantic import BaseModel
from typing import Dict, Any, List, Literal

class NodeDefinition(BaseModel):
    id: str
    category: Literal["planning", "rag", "writing", "evaluation", "export", "utility"]
    label: str
    input: Dict[str, Any]
    output: Dict[str, Any]
```
