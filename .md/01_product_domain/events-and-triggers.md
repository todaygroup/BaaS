# 이벤트 및 트리거 (Events and Triggers)

## 7.1 이벤트 카탈로그
```yaml
events:
  - id: "BookCreated"
    payload: ["book_id", "project_id", "author_id"]
  - id: "ChapterStatusChanged"
    payload: ["chapter_id", "old_status", "new_status"]
  - id: "GraphRunCompleted"
    payload: ["graph_run_id", "status", "graph_type"]
```

## 7.2 트리거 설정
```yaml
triggers:
  - on: "BookCreated"
    start_graph: "book_outline_eval_graph"
  - on: "ChapterStatusChanged"
    when:
      new_status: "researching"
    start_graph: "chapter_research_graph"
```
