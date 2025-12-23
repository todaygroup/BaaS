# 멀티 에이전트 아키텍처 (Multi-Agent Architecture)

## 7.1 에이전트 팀 구성
- **Supervisor**: 전체 워크플로우 통제.
- **Planner**: 책 구조 및 챕터 상세 계획 수립.
- **Researcher**: RAG 및 웹 검색을 통한 지식 수집.
- **Writer**: 수집된 지식을 바탕으로 풍부한 텍스트 작성.
- **Critic**: 결과물 검증 및 피드백 제공.

## 7.2 상태 공유 모델
- LangGraph의 `State`를 통해 에이전트 간 메모리 및 컨텍스트를 동기화함.
