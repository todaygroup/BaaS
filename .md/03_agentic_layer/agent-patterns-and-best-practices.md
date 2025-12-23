# 에이전트 패턴 & 베스트 프랙티스 (Agent Patterns & Best Practices)

## 8.1 Supervisor/Worker 패턴

- Supervisor:
    - Book 전체 상태 관점에서 “어떤 챕터를 언제 생성/재생성할지” 결정.
- Worker:
    - Chapter Graph를 실행해 한 챕터에 집중.

## 8.2 Reflection 패턴

- Chapter Writer → Auto Critic → (점수 < threshold) → 재작성 루프.
- GraphRecursionError 방지를 위해 iteration/step 수 제한.

```python
def eval_node(state: ChapterState) -> ChapterState:
    # ... Auto Critic 호출, eval_score 업데이트
    if state["eval_score"] < 0.8:
        state["iteration"] = state.get("iteration", 0) + 1
    return state

def route_on_eval(state: ChapterState) -> str:
    if state["eval_score"] >= 0.8:
        return "finalize"
    if state.get("iteration", 0) >= 3:
        state.setdefault("errors", []).append("Max iterations reached")
        return "finalize"
    return "research"
```
