# 실행 및 로깅 (Executions and Logging)

## 10.1 실행 모델
- `Execution`: 전체 그래프 실행 상태 기록.
- `NodeRun`: 개별 노드의 입력/출력, 토큰 사용량, 지연 시간 기록.

## 10.2 JSON 로그 스키마
```json
{
  "run_id": "...",
  "node_id": "chapter_writer",
  "latency_ms": 25000,
  "input_tokens": 5000,
  "output_tokens": 10000,
  "status": "success"
}
```
