# 관찰성 및 로깅 (Observability and Logging)

## 5.1 로그 수집 체계
- **LLMCallLog**: 모델명, 토큰, 지연시간, 성공여부.
- **GraphRunLog**: 그래프 종류, 시작/종료 시간, 최종 상태.

## 5.2 구현 예시
```python
def log_llm_call(run_id, node_id, latency, tokens):
    # JSONL 또는 DB에 기록
    pass
```
- 이 데이터를 바탕으로 챕터당 평균 비용 및 에이전트 성능을 대시보드에서 시각화함.
