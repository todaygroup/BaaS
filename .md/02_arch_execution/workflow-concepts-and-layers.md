# 워크플로우 개념 및 레이어 (Workflow Concepts and Layers)

## 4.1 워크플로우 정의
- **Book Graph**: 책 전체 자동화 (기획 → 챕터 스케줄링 → 통합).
- **Chapter Graph**: 단일 챕터 자동화 (연구 → 집필 → 평가 → 루프).

## 4.2 레이어 구성
1. **Presentation Layer**: 에디터/컨트롤 UI.
2. **Workflow Runtime Layer**: GraphRun, NodeRun 관리.
3. **Nodes & Connections Layer**: 노드/엣지 로직.
4. **Data Layer**: GraphState (Shared State).
5. **Credentials Layer**: 비밀키/자격증명 관리.
6. **Observability Layer**: 디버깅/로깅.
