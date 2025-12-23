# RAG + Agent 통합 패턴 (RAG & Agent Integration Patterns)

## 11.1 표준 패턴

- Retrieval → Relevance → Summarization → Planning/Generation.
- BAAS에서는 **Chapter Graph**에서 다음 구조 사용:
    - `research` 노드: RAG + Relevance + note 생성
    - `write` 노드: research_notes·outline 기반 초안
    - `eval` 노드: Auto Critic + 점수·피드백
    - 루프/종료: iteration/score 기준.

## 11.2 품질 평가 루프

- 각 실행에서 **question-context-answer-eval** 4요소를 구조화해 저장.
- 이후:
    - Recall/Precision 기반 통계
    - 프롬프트/임계값 튜닝
    - 지식 인덱스 보강.

```python
# /03_llm_rag_agents/eval/log_schema.py

class RAGEvalRecord(BaseModel):
    id: str
    question: str
    context_snippets: List[str]
    answer: str
    eval_score: float
    eval_feedback: str
    created_at: datetime
```
