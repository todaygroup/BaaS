<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 각 권의 전체 목차를 제 1 원칙 기반으로 먼저 설계해줘

각 권은 “이 시스템이 왜 이렇게 생길 수밖에 없는가?”를 바닥부터 설명하는 **제1원칙 → 개념 → 설계 → 구현 → 운영** 흐름으로 구성하는 게 자연스럽습니다. 아래 목차는 5권 세트 전체를 이 원칙에 맞춰 재구성한 것입니다.[^1][^2]

***

## 권 1. Product \& Domain Blueprint

### 1부. 문제 정의와 제1원칙

1. 서론: 왜 “책 한 권”을 에이전트가 써야 하는가
2. 인간 집필 프로세스의 해부
3. “정보 → 구조 → 문장”으로 본 집필의 본질
4. BAAS의 제1원칙: 계획·지식·표현·평가

### 2부. 제품 비전과 가치 가설

5. BAAS 비전·미션·North Star Metric
6. 저자/조직 관점의 Pain \& Gain 분석
7. 차별화 포인트: 일회성 LLM 사용 vs 지속적 집필 인프라[^3]
8. 성공 지표와 가설 설정

### 3부. 사용자·페르소나·유스케이스

9. 핵심 페르소나(해님, 외부 저자, 기업 컨설턴트)
10. 대표 유스케이스: 새 책 기획·리포트→책 변환·시리즈 출간[^4]
11. 세그먼트별 요구사항(개인·스튜디오·엔터프라이즈)
12. HITL(사람 개입) 포인트 설계

### 4부. 도메인 모델링

13. 엔티티 식별: Author, Workspace, Project, Book, Part, Chapter, Execution, Export
14. 관계·수명주기: Book/Chapter/Execution의 흐름
15. 도메인 이벤트: BookCreated, ChapterStatusChanged, GraphRunCompleted
16. Book/Chapter JSON 스키마 및 Pydantic 모델 전체

### 5부. 정보 아키텍처 \& URL 구조

17. Workspace → Project → Book → Chapter → Execution → Export 계층
18. Navigation/URL 설계 규칙
19. 정보 구획: Dashboard, Book Overview, Chapter Workspace, Settings
20. Next.js 라우팅/슬러그 패턴 정의

### 6부. 요구사항 명세

21. 기능 요구사항: 기획·RAG·집필·편집·평가·Export
22. 비기능 요구사항: 성능·안정성·품질·재현성·보안[^5]
23. 요구사항 → 도메인/그래프/UX 매핑 테이블
24. 릴리즈 슬라이스(Vertical Slice) 로드맵

### 7부. 아티팩트 \& 예제

25. PRD v1.0 전문
26. 도메인 모델 예제 코드 모음
27. Book/Chapter 샘플 JSON·YAML
28. 설계 리뷰 체크리스트

***

## 권 2. Architecture \& Execution Engine

### 1부. 시스템 아키텍처 제1원칙

1. 에이전트 시스템의 본질: 모델·도구·지시·상태[^6][^7]
2. BAAS에서 “생각하는 레이어”와 “전달 레이어” 분리
3. Agentic 아키텍처 공통 패턴 요약[^8][^9]
4. BAAS 전체 레퍼런스 아키텍처 개요

### 2부. 기술 스택 \& 제약

5. 언어/프레임워크 선택 근거(Python, TS, LangGraph 등)
6. LLM Provider/OpenRouter, RAG, DB, 인프라 선택 원칙[^1]
7. 비용·규제·팀 역량 제약 분석
8. 스택별 책임·경계 정의

### 3부. C4 아키텍처

9. 시스템 컨텍스트 다이어그램
10. 컨테이너 다이어그램(Web, API, Worker, DB, Vector)
11. 핵심 컴포넌트 다이어그램(Workflow Engine, RAG, Observability)
12. 모듈화 전략(모놀리식 vs 모듈러 모노레포 vs 서비스 분리)

### 4부. 워크플로우 \& 런타임 모델

13. “미니앱 = 그래프 + 상태” 개념 정립
14. Book Graph / Chapter Graph / Eval Graph 설계 원칙[^10][^11]
15. Workflow Runtime: GraphRun, NodeRun, Execution 모델
16. 의존성·멱등성·재시도·Timeout 설계

### 5부. 노드·연결·데이터 구조

17. 노드 타입: Trigger / Action / Core Logic / Subgraph
18. 노드 인터페이스: 입력·출력·옵션·에러 동작
19. 연결 패턴: 직선형·브랜치·루프·합류[^12]
20. GraphState 설계와 TypedDict 전략

### 6부. LangGraph 구현

21. LangGraph StateGraph 구조와 BAAS 매핑[^11][^13]
22. Book Graph 전체 코드
23. Chapter Graph 전체 코드(루프·Eval 포함)
24. Eval Graph/품질 게이트 구현

### 7부. 실행·디버깅·Observability 훅

25. 실행 모델: 동기/비동기, 백그라운드 작업, 큐 사용 여부
26. 실행 로그 구조와 OpenTelemetry 통합[^14][^15]
27. 데이터 핀닝·리플레이·모킹 기법
28. 아키텍처/엔진 레벨 체크리스트

***

## 권 3. LLM · RAG · Agentic Layer

### 1부. 제1원칙: LLM·RAG·Agent 역할 분리

1. LLM이 하는 일과 한계(지식/컨텍스트/랜덤성)[^16]
2. RAG의 필요성: 사실성·개인화·스케일
3. Agentic 패턴: Planner / Worker / Reviewer / Router[^9][^8]
4. BAAS에 필요한 인지 능력 정의

### 2부. LLM Layer 설계

5. 모델 선택 기준(품질·비용·길이·언어)
6. 역할별 모델 매핑 표(gpt-4.1, mini, Claude, o3 등)[^17]
7. OpenRouter 기반 공통 호출 레이어 설계
8. 토큰·비용·Latency 관리 전략

### 3부. 프롬프트 아키텍처 \& Role 체계

9. developer/system/user/assistant/tool 역할 정의와 우선순위[^18][^19]
10. 역할별 포함/제외해야 할 내용
11. BAAS 전역 developer prompt 설계
12. Book/Chapter/Research/Eval용 system/user 템플릿

### 4부. Prompt 라이브러리 \& 버전 관리

13. /prompts/developer, /system, /user, /tool 구조
14. 프롬프트 메타데이터(목적, 버전, 관련 그래프)
15. 실험·A/B 테스트 전략 및 계측[^17]
16. 변경 관리와 롤백 절차

### 5부. 멀티에이전트 설계

17. BAAS 에이전트 팀 정의(Book Supervisor, Planner, Research 등)[^11]
18. 각 에이전트 책임·입출력 스키마·실패 규칙
19. 에이전트 간 핸드오프와 상태 공유 설계
20. Supervisor/Worker, Router, Reflection 패턴 구현[^9][^10]

### 6부. RAG \& Knowledge Engineering

21. 지식 계층 아키텍처: 원본 → 청크 → 임베딩 → 벡터스토어[^20]
22. PDF/노트 파이프라인: 추출·클리닝·Chunking·임베딩
23. 메타데이터 스키마(Part/Chapter, 레벨, 토픽 등)
24. Hybrid Retrieval + 필터/랭킹 전략[^21]

### 7부. Relevance Checker \& 평가 루프

25. Relevance Checker 역할·입출력·임계값 설계[^22]
26. LangChain Runnable 구현 및 프롬프트 템플릿
27. LangGraph 라우팅: retrieve → relevance → 재검색/생성[^23]
28. 질문-문맥-응답-평가 데이터 저장·튜닝

### 8부. LLM·RAG·Agent 레이어 통합

29. Book/Chapter 플로우에서의 LLM/RAG/Agent 협업 시퀀스
30. 품질·비용·안전성 밸런싱 전략[^24][^12]
31. 전체 레이어 코드 구조 정리
32. 진화 전략(새 모델·새 에이전트·새 도메인 추가)

***

## 권 4. Delivery Stack (Backend · Frontend · DevOps)

### 1부. Delivery Stack의 제1원칙

1. “지능”에서 “서비스”로: 전달 계층의 역할[^3]
2. 사용자–API–모델–데이터 사이의 경로 재구성[^1]
3. BAAS Delivery의 핵심 요구: 신뢰·속도·안정성

### 2부. Monorepo \& 모듈 구조

4. apps/web, apps/api, apps/worker, packages/* 구조 설계
5. 코드 소유권·경계·디펜던시 규칙
6. 환경별 설정(dev/stage/prod) 전략[^25]

### 3부. Backend (FastAPI + LangGraph)

7. 라우터/서비스/리포지토리/스키마 레이어 구조
8. 도메인별 API 설계(Books, Chapters, Executions, Exports)
9. LangGraph 엔드포인트 패턴(sync/async, 장기 실행)[^13]
10. 외부 통합(ESP, Slack, Stripe, CRM) 모듈 설계

### 4부. Frontend (Next.js PWA)

11. App Router 구조와 route group 설계
12. RSC vs Client Component 전략과 데이터 패칭[^26]
13. 상태·캐싱·에러 처리(TanStack Query/SWR)
14. Workflow/Execution UI(타임라인·로그·Draft Viewer)

### 5부. DevOps \& CI/CD

15. 환경변수/Secrets 관리 전략(Vault, GitHub Actions 등)[^5]
16. 빌드·테스트·배포 파이프라인 설계[^27][^28]
17. 배포 전략: Vercel/Cloud Run/K8s, Canary/Blue-Green
18. 롤백·마이그레이션·백업 전략

### 6부. 비용·성능 최적화

19. LLM 비용 모니터링·예산 가드 레일[^24]
20. 캐싱·저비용 모델·배치 처리 전략[^12]
21. 인프라 스케일링(오토스케일, 멀티리전)
22. 비용 대시보드·리포트 설계

### 7부. 운영 관점의 Delivery

23. 장애 대응에서 Delivery Stack의 역할
24. 배포/실행/관측 일체화(Release+Observability)
25. 보안·권한·감사 로깅
26. 운영 체크리스트

***

## 권 5. UX · Interaction · Ops Runbook

### 1부. BAAS UX의 제1원칙

1. 장기 실행 AI 작업의 UX 과제[^29][^30]
2. LLM-first 제품 UX 설계 방향[^31][^3]
3. BAAS 사용자 여정(User Journey) 정의

### 2부. UX 원칙 \& 화면 설계

4. 글로벌 UX 원칙(일관성·피드백·오류 복구·접근성)[^32]
5. 네비게이션 모델(대시보드/에디터/설정/리포트)
6. 각 화면 와이어프레임(대시보드, Book, Chapter, Execution, Settings)

### 3부. Prompt UX \& Vibe Coding

7. Prompt UX의 제1원칙(맥락·제약·예시)[^33][^34]
8. Vibe Coding 플로우(Describe → Plan → Scaffold → Refine → Test → Document)[^35]
9. 입력/출력 UX 패턴(폼, 프리셋, 플레이북)
10. Prompt Playbook(아키텍처 리뷰, 리팩토링, 버그 재현 등)

### 4부. Observability \& Logging

11. LLM·Graph·RAG용 로그/메트릭 설계[^15][^14]
12. 분산 트레이싱과 장기 실행 모니터링[^36][^37]
13. 대시보드 설계(운영/경영/제품 관점)
14. 알람 전략(임계값·노이즈 제어)

### 5부. AI 평가 \& 피드백 루프

15. AgentEval 설계(지표, 프롬프트, 파이프라인)[^38][^39]
16. 사용자 피드백(평점·코멘트) 수집·통합
17. 품질 리포트·회고 사이클
18. 프롬프트/모델/RAG 개선 워크플로우

### 6부. 거버넌스 \& 리스크 관리

19. 정책·가이드라인(안전·보안·규제)[^40][^5]
20. 변경 관리(모델/프롬프트/그래프/인덱스 버전닝)
21. 감사 로그·접근 제어·PII 처리[^24]
22. 책임·역할·승인 플로우

### 7부. Ops Runbook \& 확장

23. 장애 유형별 Runbook(LLM/RAG/DB/외부 통합)
24. 인시던트 프로세스·에스컬레이션·커뮤니케이션[^36]
25. 기능·성능·조직 확장 시나리오
26. BAAS 운영 체크리스트 \& 베스트 프랙티스

***

이 목차들을 그대로 각 디렉터리별 `README.md` 상단에 “권 전체 목차”로 두고, 하위 `.md`들은 이 장·절 구조에 맞춰 나누면 전체 BAAS 백서 세트가 자연스럽게 맞물립니다.[^8][^1]
<span style="display:none">[^41][^42][^43][^44][^45][^46]</span>

<div align="center">⁂</div>

[^1]: https://www.systemdesignhandbook.com/guides/llm-system-design/

[^2]: https://explained-from-first-principles.com

[^3]: https://blog.logrocket.com/designing-llm-first-products/

[^4]: https://vlinkinfo.com/blog/guide-to-llm-product-development

[^5]: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/ANSSI-BSI-joint-releases/LLM-based_Systems_Zero_Trust.pdf?__blob=publicationFile\&v=3

[^6]: https://akka.io/blog/agentic-ai-architecture

[^7]: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

[^8]: https://gerred.github.io/building-an-agentic-system/

[^9]: https://github.com/PacktPublishing/Building-Agentic-AI-Systems

[^10]: https://blog.langchain.com/langgraph-multi-agent-workflows/

[^11]: https://langchain-ai.github.io/langgraph/concepts/multi_agent/

[^12]: https://eugeneyan.com/writing/llm-patterns/

[^13]: https://www.langchain.com/langgraph

[^14]: https://dl.acm.org/doi/10.1145/3706599.3719914

[^15]: https://apxml.com/courses/mlops-for-large-models-llmops/chapter-5-llm-monitoring-observability-maintenance/llm-logging-observability

[^16]: https://naina0405.substack.com/p/very-important-llm-system-design-d42

[^17]: https://www.ai21.com/blog/llm-product-development/

[^18]: https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case/leveraging-system-user-and-assistant-roles-for-better-prompts

[^19]: https://practiqai.com/blog/system-prompts-roles-instruction-hierarchy

[^20]: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/

[^21]: https://www.siddharthbharath.com/build-deep-research-agent-langgraph/

[^22]: https://wikidocs.net/267810

[^23]: https://www.swarnendu.de/blog/langgraph-best-practices/

[^24]: https://galileo.ai/blog/understanding-llm-observability

[^25]: https://www.prioxis.com/blog/llm-product-development

[^26]: https://www.pronextjs.dev/workshops/next-js-react-server-component-rsc-architecture-jbvxk/understanding-the-example-monorepo-structure-4gpny

[^27]: https://forum.cursor.com/t/best-practices-for-structuring-a-next-js-fastapi-supabase-project/49706

[^28]: https://github.com/belgattitude/nextjs-monorepo-example/blob/main/README.md

[^29]: https://particula.tech/blog/long-running-ai-tasks-user-interface-patterns

[^30]: https://developer.atlassian.com/platform/forge/llm-long-running-process-with-forge-realtime/

[^31]: https://arxiv.org/html/2507.04469v1

[^32]: https://uxdesign.cc/thinking-past-the-cliche-of-llms-ai-design-patterns-c9b849fce9e8

[^33]: https://www.gocodeo.com/post/prompt-ux-in-vibe-coding-a-new-frontier-for-software-design

[^34]: https://emergent.sh/learn/vibe-coding-prompts

[^35]: https://uxdesign.cc/cracking-the-code-of-vibe-coding-124b9288e551

[^36]: https://lantern.splunk.com/Observability_Use_Cases/Troubleshoot/Automating_alert_investigations_by_integrating_LLMs_with_the_Splunk_platform_and_Confluence

[^37]: https://www.logicmonitor.com/blog/ai-observability

[^38]: https://leehanchung.github.io/blogs/2024/05/22/first-principles-eval/

[^39]: https://www.clarifai.com/blog/agentic-prompt-engineering

[^40]: https://petronellatech.com/blog/monitor-secure-scale-the-enterprise-playbook-for-llm-observability/

[^41]: https://arxiv.org/pdf/2507.10281.pdf

[^42]: https://play.google.com/store/books/details/Designing_Agentic_AI_Architecture_and_Development_?id=lcxlEQAAQBAJ\&hl=am

[^43]: https://thita.ai/blog/ai/ai-llm-roadmap-patterns

[^44]: https://orq.ai/blog/llm-product-development

[^45]: https://dev.to/ezinsightsai/llm-product-development-in-2025-the-ultimate-guide-37f1

[^46]: https://www.reddit.com/r/learnmachinelearning/comments/1glkkve/faang_ml_system_design_interview_guide/

