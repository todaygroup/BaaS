# 연결 및 흐름 제어 (Connections and Flow Control)

## 7.1 기본 패턴
- **직선형**: 단순 순차 실행.
- **브랜치/합류**: 조건문 및 병렬 노드 대기.
- **루프**: Eval 점수 기반 재시도 루프.

## 7.2 LangGraph 예시
```python
# Chapter Graph with Loop
def route_on_eval(state: ChapterState) -> str:
    if state["eval_score"] >= 0.8 or state["iteration"] >= 3:
        return END
    return "research"

workflow = StateGraph(ChapterState)
workflow.add_node("research", research_node)
workflow.add_node("write", write_node)
workflow.add_node("eval", eval_node)

workflow.set_entry_point("research")
workflow.add_edge("research", "write")
workflow.add_edge("write", "eval")
workflow.add_conditional_edges("eval", route_on_eval, {END: END, "research": "research"})
```
