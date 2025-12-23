# LangGraph 백엔드 통합 (LangGraph Backend Integration)

## 3.3 그래프 실행 API
- API를 통해 `BookGraph` 및 `ChapterGraph`를 비동기로 실행하고 상태를 기록함.

```python
@router.post("/book/run")
async def run_book(payload: BookInput, graph=Depends(get_book_graph)):
    initial_state = {"topic": payload.topic, "audience": payload.audience}
    result = await graph.ainvoke(initial_state)
    return result
```

## 3.4 실행 상태 추적
- `ExecutionRepo`를 통해 그래프의 `run_id`별 상태(pending, running, success, fail)를 DB에 저장하고 프론트엔드에 노출함.
