# 프로덕션 준비 체크리스트 (Production Readiness Checklist)

BAAS AI Agent 서비스를 출시하기 전에 거쳐야 할 최종 검토 및 최적화 절차입니다.

## 1. Product · 도메인 레벨
- [ ] 핵심 유스케이스(기획, 집필, 통합) UI/API 대응 확인.
- [ ] 상태 전이(planned → final) 일관성 검증.
- [ ] 유저 여정 및 HITL(Human-In-The-Loop) 포인트 점검.

## 2. 아키텍처 · LangGraph 엔진
- [ ] 그래프 구조 시각화 및 복잡도 평가.
- [ ] 스텝 제한(iteration) 및 무한 루프 차단 로직 확인.
- [ ] 에러 경로 및 Fallback(재시도/중단) 시나리오 검증.

## 3. LLM · 프롬프트 · RAG
- [ ] 역할별 모델 매핑 및 파라미터(temperature 등) 최적화.
- [ ] 프롬프트 아키텍처(developer/system/user) 견고화.
- [ ] RAG 품질(Chunking, Retrieval) 및 Relevance Checker 임계값 튜닝.
- [ ] AgentEval 데이터셋 기반 품질 벤치마킹.

## 4. 테스트 · 관찰성 · 안정성
- [ ] 테스트 커버리지(Unit, Graph, Eval, E2E) 갭 분석.
- [ ] LLM 호출 로그 및 분산 트레이싱(Trace ID) 연동.
- [ ] 성공률, 비용, 지연시간 메트릭 대시보드 구축.

## 5. 보안 · 거버넌스 · 운영
- [ ] 12-Factor 기반 환경 설정 및 Secret Manager 점검.
- [ ] 민감 데이터(PII) 마스킹 및 보안 스캔.
- [ ] 장애 대응 런북(Runbook) 최신화.

## 6. UX · 사용자 경험
- [ ] 장기 실행 작업 진행 상태 표시 및 중단 기능.
- [ ] Prompt UX(입력 가이드, 템플릿) 최적화.
- [ ] 사용자 피드백 루프(Good/Bad) 연동.

## 7. 론치 및 롤아웃
- [ ] 파일럿 그룹 대상 만족도 및 품질 측정.
- [ ] 점진적 기능 활성화(Feature Flag) 전략 수립.
- [ ] 모델/프롬프트 업데이트 관리 프로세스 확립.
