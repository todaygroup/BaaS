# 배포 & 비용 최적화 (Deployment & Cost Optimization)

## 5.3 배포 전략 & 비용 최적화

- **API/Worker**: Cloud Run / ECS / K8s 중 선택.
- **Web**: Vercel / Static Export.
- LLM 비용 줄이기:
    - Dev 환경: gpt-4.1-mini / o3-mini 사용.
    - RAG로 컨텍스트 최소화, 요약 체인 삽입.
    - AgentEval/AutoCritic도 “샘플 실행만 평가” 전략.
