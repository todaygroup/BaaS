# 워크플로우 내 데이터 모델 (Data Model in Workflows)

## 8.1 GraphState 설계 지침
- **TypedDict**를 사용해 상태 타입을 정의하고, 각 노드는 상태의 특정 키를 반환하여 상태를 업데이트함.
- 상태는 노드 간 데이터 전달의 유일한 통로.

## 8.2 ChapterState 예시
```python
class ChapterState(TypedDict, total=False):
    chapter_id: str
    book_id: str
    outline: dict
    research_notes: list
    draft_text: str
    eval_score: float
    iteration: int
```
