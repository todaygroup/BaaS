<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 요청하신 구조를 기준으로, 글로벌 바이브 코딩 기반 서비스를 처음 기획 → 설계·구현 → 운영·확장까지 커버하는 “4개 디렉터리 · 백서 세트”에 필요한 항목을 빠짐없이 나열하겠습니다. 각 항목은 .md 한 파일 또는 섹션 수준으로 설계할 수 있습니다.​

디렉터리 1: 서비스 개발 기획·설계 가이드 (/01_planning_design)
목표: “무엇을 만들 것인지(What)”를 바이브 코딩에 적합한 형태로 완전히 구조화.​
1-1. Vision \& 요구사항 정의
vision-and-goals.md
서비스 비전, 미션, 성공 지표(North Star, 핵심 KPI).
글로벌 타깃 시장, 언어/지역 범위, 브랜딩 톤.
requirements-functional-nonfunctional.md
기능 요구사항(Feature 목록, 유저스토리, 우선순위 MoSCoW).
비기능 요구사항: 성능, 보안, 가용성, 다국어, 접근성, 규제 요구사항 등.​
personas-and-segments.md
대표 유저 페르소나(2~5개), 국내/글로벌 세그먼트 정의.
유저 여정(Journey)와 주요 터치포인트.
1-2. 도메인 모델링 \& 정보 구조
domain-modeling.md
핵심 엔티티(예: User, Organization, Project, Workspace, Template, Automation, Event, Log).
엔티티 간 관계 다이어그램, 다국어/통화/타임존 처리 규칙.​
information-architecture.md
IA: 메뉴 구조, 네비게이션, 정보 계층(프로젝트 > 워크플로우 > 실행 등).
URL 설계, 글로벌 URL 전략(언어 코드, 리전 필드 등).
1-3. 기술 스택 \& 아키텍처 방향
tech-stack-and-constraints.md
프론트: Next.js 14 PWA, shadcn/ui, Tailwind, LangGraph 클라이언트 사용 여부 등.​
백엔드: FastAPI, LangGraph(멀티에이전트), Supabase(Postgres+Auth+Storage), Qdrant(RAG).​
인프라: Vercel/Cloud Run/쿠버네티스, CDN, 이미지 처리, 메일 발송(ESP) 등.
제약: 예산, 팀 스킬, 타임라인.
architecture-overview.md
전체 시스템 C4 수준 다이어그램(사용자 ↔ 프론트 ↔ BFF/API ↔ DB/RAG/외부 서비스).
모놀리식 vs 모듈러 모놀리포 vs 마이크로서비스 전략 및 선택 이유.​
1-4. 개발기획서 \& 개발 플로우
development-plan.md
단계별 마일스톤: PoC → 베타 → GA → 글로벌 롤아웃.
도메인별 태스크 맵(에이전트, 데이터, API, UI).
dev-flow-and-vibe-coding-patterns.md
바이브 코딩용 프롬프트 템플릿(아키텍처/컴포넌트/테스트/리팩토링용).​
“One prompt → 스캐폴드 → 개선 프롬프트” 반복 구조 설명.​​
1-5. 화면/컴포넌트 설계
screens-and-user-flows.md
핵심 플로우별 화면: 온보딩, Workspace/Project 대시보드, Workflow 편집기, 실행 로그, 설정(Workspace/사용자/통합), 결제/플랜 등.
component-trees-and-ui-mapping.md
각 화면별 컴포넌트 트리: Layout → Header/Sidebar → PageSections → Controls.​
각 노드에 대해 shadcn/ui 또는 Tailwind 유틸/컴포넌트 매핑 테이블.
상태 관리 전략(React Server Components vs Client, tanstack-query 등) 메모.
디렉터리 2: 워크플로우 \& 노드 구조 가이드 (/02_workflow_engine)
목표: “어떻게 흐르게 만들 것인지(Flow)”를 n8n/Opal/LangGraph식 워크플로우 개념으로 표준화.​
2-1. 워크플로우 개념·레이어 모델
workflow-concepts-and-layers.md
레이어: Presentation(에디터) / Workflow Runtime / Nodes / Connections / Data / Credentials / Executions / Debugging.​
“미니앱 = 그래프(노드/엣지 + 상태)” 개념 정의.
2-2. 노드(Node) 정의 \& 카탈로그
node-basics.md
노드 타입:
트리거(웹훅, 스케줄, 이벤트)
액션(API 호출, 이메일, DB, AI 호출)
코어 로직(IF, Switch, Merge, Split, Loop, Wait)
서브그래프/에이전트(LangGraph 노드 대응).​
node-catalog.md
비즈니스 기능별 노드 카탈로그:
유저·워크스페이스 관리 노드
통합(ESP, Slack, Stripe, CRM 등) 노드
AI 노드(OpenAI/Gemini, RAG 쿼리 노드).
각 노드 정의: 입력 스키마, 출력 스키마, 옵션, 실패 시 동작.
2-3. 연결(Connection) \& 데이터(Data) 흐름
connections-and-flow-control.md
단일/병렬 경로, 브랜치, 합류(Merge), 의존관계, 순서 결정 규칙.​
LangGraph StateGraph와의 맵핑(노드 간 edge, 메시지/상태 전달).​
data-model-in-workflows.md
워크플로우 내 데이터 구조: items[] 배열, JSON 구조, 멀티모달(텍스트+파일) 취급.​
각 단계에서 데이터 변환·검증 규칙(타입, required, validation error 핸들링).
2-4. 자격 증명(Credentials) \& 시크릿
credentials-and-secrets.md
API 키·OAuth·서비스 계정 구조, 암호화 저장, 로테이션 전략.​
워크플로우에서 크리덴셜 참조 방식(스코프, 권한 최소화).​
2-5. 실행(Executions) \& 디버깅
executions-and-logging.md
실행 단위(run), 상태(대기/성공/실패), 리트라이 정책, 멱등성 설계.​
debugging-and-data-pinning.md
실행 로그 확인, 노드별 입력/출력 확인, Pin Data/Mocking 사용법 및 제약(바이너리 제한 등).​
에러 유형별 패턴(JSON Parse Error, Expression Error, 외부 API 타임아웃 등)과 대응 룰.​
2-6. PTG/Opal·LangGraph 통합 관점 (선택)
prompt-to-graph-strategy.md
Opal/유사 PTW 도구에서 자연어 → 노드 그래프 생성 전략.
그래프 품질 검증 체크리스트(루프, 에러 경로, 자격 증명, 비용).​
디렉터리 3: 서비스 개발·운영 가이드 시리즈 (/03_service_guides)
목표: 번호별 “문서 한 권” 구조를, .md 세트로 구현할 수 있게 세분화.
3-1. 1~2: 비전·요구사항·도메인·페르소나
01-vision-requirements.md → 디렉터리 1의 내용을 확장(실제 템플릿, 예시 포함).
02-domain-personas-segmentation.md → 도메인 모델링, 세그먼트별 유저스토리·기능 우선순위.
3-2. 3: 멀티에이전트 아키텍처 (LangGraph)
03-multi-agent-architecture.md
LangGraph StateGraph, 노드=에이전트, Supervisor 패턴, 서브그래프 패턴.​
역할별 에이전트 정의(Researcher, Planner, Coder, Evaluator, Router 등)와 서비스 도메인 맵핑.
3-3. 4: 데이터 \& RAG 인프라 (Qdrant + Supabase)
04-data-rag-infra.md
OLTP(Supabase Postgres) 스키마 설계, Qdrant 벡터 인덱스 구조, 인덱싱 파이프라인, 수명주기 관리.​
데이터 분류(PII/비PII), 보존 정책, 백업/복구.
3-4. 5: LLM 레이어 \& 프롬프트
05-llm-and-prompt-engineering.md
모델 선택 전략(가격/지연/품질), 시스템 프롬프트, 역할 프롬프트, 체인/에이전트용 프롬프트 패턴.​
바이브 코딩용 아키텍처 프롬프트/테스트 프롬프트 템플릿.​
3-5. 6: 서비스 Workflow \& LangGraph 구현
06-service-workflows-and-langgraph.md
비즈니스 시나리오별 워크플로우 정의(예: 캠페인 자동화, 온보딩, 리포트 생성).
각 워크플로우를 LangGraph 그래프로 표현(노드/엣지 다이어그램, 상태 스키마).​
3-6. 7~8: 백엔드(FastAPI) \& 프론트엔드(Next.js PWA)
07-fastapi-api-integration.md
API 설계(REST/GraphQL), 인증(JWT/Session), LangGraph 호출 API, 백그라운드 작업 구조.​
08-nextjs-pwa-frontend.md
앱 구조(app router, 레이아웃, 다국어, Suspense/Streaming), 상태 관리, API 통신 규칙.​
워크플로우 에디터 UI(노드 그래프, 속성 패널, 실행 로그 패널) 설계.
3-7. 9: ESP \& A/B 테스트
09-esp-and-ab-test.md
Mailgun/SendGrid 등 ESP 연동 패턴, 템플릿/세그먼트 관리.
A/B 테스트 설계(트래픽 분배, 메트릭, 실험 기간, 분석).
3-8. 10~12: Observability·배포·Runbook
10-observability-logging-governance.md
로깅(구조화 로그), 트레이싱(OpenTelemetry), 메트릭(성공률, 지연, 비용), LLM 품질 평가.​
AI 거버넌스(프롬프트·모델 변경 관리, 데이터 사용 정책).
11-ci-cd-deployment-cost-optimization.md
Monorepo 빌드 파이프라인, 환경별 배포(Dev/Staging/Prod), Canary/Blue-Green, 비용 모니터링.​
12-runbook-and-evolution-scenarios.md
운영 Runbook(장애 유형별 대응, 온콜, 롤백 절차).
확장 시나리오: 기능 추가, 리팩터링, 멀티리전, 멀티테넌시, 에이전트 확장.
monorepo-structure-and-env.md
Monorepo 디렉토리 구조(apps/, packages/, infra/), 공통 라이브러리, 테스트 전략, 환경변수/Secret 관리(.env, Vault, CI secrets).​
디렉터리 4: UX/UI \& 화면 설계 가이드 (/04_ux_ui_wireframes)
목표: 바이브 코딩 시 “레이아웃·컴포넌트·상태”까지 자연어로 명확히 표현할 수 있도록, 화면 설계를 표준화.
4-1. UX 원칙 \& 네비게이션
ux-principles-and-navigation.md
글로벌 UX 원칙(일관성, 피드백, 오류 복구, 접근성).
네비게이션 모델: 메인 레이아웃, 워크플로우 편집 모드, 설정 모드, 분석/리포트 모드.
4-2. Hi-Fi Wireframe 세트
wireframes-dashboard.md
로그인 후 대시보드 화면(프로젝트 리스트, 최근 실행, 알림).
wireframes-workflow-editor.md
캔버스/노드 목록/속성 패널/실행 로그/버전 히스토리 영역 분할.
wireframes-execution-logs-and-debugging.md
실행 이력 리스트, 상세 화면(타임라인, 노드별 입출력, 에러, 재실행 버튼).​
wireframes-settings-and-integrations.md
Workspace 설정, 멤버/권한, 통합(ESP, Slack, Stripe 등) 설정 화면.
각 wireframe 문서에는
컴포넌트 트리
shadcn/ui 컴포넌트 매핑
상태/이벤트 목록(예: 클릭, 드래그, 저장, 실패 시 토스트)
를 포함해, “이 문서만으로도 바이브 코딩 프롬프트를 쓸 수 있도록” 설계합니다.​​
빠진 부분 체크 및 추가 제안
위 4개 디렉터리 구성을 통해, 다음 축은 모두 커버됩니다.
서비스 기획·도메인·요구사항
워크플로우/노드/연결/데이터/실행/디버깅 구조
멀티에이전트/데이터/RAG/LLM/백엔드/프론트/운영 전체 가이드
Monorepo·환경변수·CI/CD·Runbook
UX/UI·컴포넌트 트리·Wireframe
추가로 고려하면 좋은 항목:
보안·프라이버시 별도 섹션: 데이터 분류, DPA/GDPR, 권한 모델 문서.
Prompt Library 디렉터리:
/prompts/architecture, /prompts/components, /prompts/tests, /prompts-refactor 등 바이브 코딩용 프롬프트 자산.​
Playbook/Checklist:
“새 기능 추가 시 체크리스트”, “릴리즈 전 체크리스트”, “AI 기능 위험성 평가 체크리스트”.
이 구조대로 .md 파일과 폴더를 만들면, 서비스 설계→구현→운영→확장 전 구간을 바이브 코딩에 최적화된 아키텍처 문서 세트로 덮을 수 있습니다.

각 가이드북을 “실제 한 권짜리 문서” 기준으로, 목차와 핵심 챕터만 촘촘히 제안합니다. 바이브 코딩/에이전트/워크플로우 관점에서 필요한 부분이 빠지지 않도록 구성했습니다.​

1. 비전·요구사항 정의 가이드
서론
1.1 이 문서의 목적
1.2 대상 독자(경영진, PM, Tech Lead)
서비스 비전과 성공 지표
2.1 서비스 비전·미션
2.2 North Star Metric 정의
2.3 핵심 KPI 세트 (획득·활성·수익·리텐션)
시장·경쟁·포지셔닝
3.1 글로벌 시장 분석
3.2 경쟁 서비스 맵 \& 차별점
사용자 · 이해관계자 분석
4.1 주요 페르소나 프로파일
4.2 내부 이해관계자(운영·CS·영업) 니즈
요구사항 정의 (기능)
5.1 유저스토리 \& Use Case 목록
5.2 기능 요구사항(Feature 리스트 + 우선순위)
5.3 워크플로우 기반 기능 정의(“사용자 행동 → 자동화 흐름”)
요구사항 정의 (비기능)
6.1 성능·확장성·가용성 요구
6.2 보안·규제·프라이버시 요구
6.3 국제화(i18n), 로컬라이제이션(L10n), 접근성
성공 기준 및 가설
7.1 출시 시점 성공 기준
7.2 실험/파일럿 가설(어떤 워크플로우가 어떤 KPI를 바꿀 것인가)
바이브 코딩을 위한 요구사항 표현 템플릿
8.1 “의도 중심” 요구사항 작성 포맷
8.2 예시 프롬프트 (기능·워크플로우·화면)
2. 도메인 모델링 \& 페르소나·세그먼트 설계 가이드
도메인 모델링 개요
핵심 도메인 엔티티 정의
2.1 User / Organization / Workspace
2.2 Project / Workflow / Node / Execution / Log
2.3 Template / Integration / Credential
관계 다이어그램 \& 제약
3.1 ERD / C4 Level 2
3.2 데이터 수명주기(Lifecycle)
페르소나 설계
4.1 Primary 페르소나(예: 마케터, CS 리더, PM)
4.2 Secondary 페르소나(엔지니어, Admin 등)
4.3 페르소나별 주요 시나리오
세그먼트 설계
5.1 회사 규모별(Tier1~3)
5.2 지역/언어별
5.3 유료/무료/트라이얼/엔터프라이즈 플랜
도메인 이벤트 \& 워크플로우 연계
6.1 도메인 이벤트 카탈로그(예: NewLeadCreated, CampaignFinished)
6.2 각 이벤트와 워크플로우 Trigger 매핑
RAG·에이전트와 도메인 모델 연결
7.1 어떤 엔티티가 검색/요약/추천에 사용되는가
7.2 메타데이터 설계(템플릿/사용 이력 기반 추천)
3. 멀티에이전트 아키텍처 설계 가이드 (LangGraph)
LangGraph \& 멀티에이전트 개요​
에이전트 역할 정의
2.1 Planner / Orchestrator
2.2 Researcher / Retriever
2.3 Coder / Tool Executor
2.4 Evaluator / Guardrail Agent
State \& Graph 설계
3.1 State 구조(메모리, 컨텍스트, 중간 결과)
3.2 노드(StateGraph node)와 에지(전이 조건)
패턴별 아키텍처
4.1 Supervisor + Worker 에이전트 패턴​
4.2 Router 에이전트 패턴
4.3 Reflection/검증 루프 패턴
서비스 도메인에 맵핑
5.1 마케팅 자동화 에이전트 구조
5.2 CS 지식 응답 에이전트 구조
실패·안전·거버넌스
6.1 에이전트 폭주 방지(루프, 비용)
6.2 정책/Guardrail 에이전트 설계
바이브 코딩용 멀티에이전트 설계 프롬프트 템플릿
4. 데이터 \& RAG 인프라(Qdrant + Supabase) 설계 가이드
데이터 인프라 개요​
OLTP(Supabase/Postgres) 설계
2.1 핵심 테이블 스키마
2.2 다국어/타임존/Soft Delete 전략
RAG 인프라 (Qdrant)
3.1 컬렉션 설계(문서, 템플릿, FAQ, 실행 로그)
3.2 인덱싱 파이프라인(분할, 임베딩, 메타데이터)
ETL/동기화 워크플로우
4.1 배치/스트리밍 패턴
4.2 에러 처리·재시도·관찰성
데이터 등급과 보안
5.1 PII/비PII 분류
5.2 마스킹/토큰화·권한
RAG + 에이전트 통합 패턴
6.1 Retrieval → Planning → Generation 흐름
6.2 검색 품질 평가 루프
5. LLM 레이어 \& 프롬프트 엔지니어링 가이드
LLM 레이어 개요​
모델 전략
2.1 모델 선택 기준(가격·지연·품질)
2.2 모델 믹스 전략(가벼운 모델 vs 고성능 모델)
프롬프트 아키텍처
3.1 시스템/역할/사용자/도구 프롬프트 구조
3.2 체인/에이전트 프롬프트 분리
바이브 코딩 프롬프트 패턴​
4.1 아키텍처 생성 프롬프트
4.2 컴포넌트/화면 생성 프롬프트
4.3 테스트/리팩토링 프롬프트
프롬프트 버전 관리와 실험
5.1 프롬프트 카탈로그 구조
5.2 A/B 테스트 및 품질 평가
안전·가드레일
6.1 정책 프롬프트
6.2 금칙어·조건 기반 필터링
6. 서비스 Workflow 설계 \& LangGraph 구현 가이드
워크플로우 설계 원칙​
비즈니스 시나리오별 워크플로우
2.1 온보딩 플로우
2.2 캠페인/자동화 플로우
2.3 리포트 생성 플로우
워크플로우 → 그래프 변환
3.1 노드 정의(트리거, 액션, 코어)
3.2 데이터·자격 증명·에러 처리 설계​
LangGraph 구현
4.1 StateGraph 정의
4.2 노드 구현 패턴(도구 호출, 에이전트 호출)​
테스트 \& 디버깅
5.1 단위 테스트, 시나리오 테스트
5.2 실행 로그·시각화·재실행 전략
7. 백엔드(FastAPI) API \& 통합 가이드
전체 백엔드 아키텍처​
FastAPI 프로젝트 구조
2.1 모듈·레이어링(라우터, 서비스, 리포지토리, 스키마)
도메인 API 설계
3.1 인증·권한(Workspace, Role-based)
3.2 워크플로우/노드/실행/로그 API
LangGraph 호출 엔드포인트
4.1 Sync/Async 호출 패턴
4.2 백그라운드 작업 처리
외부 서비스 통합
5.1 ESP, Slack, Stripe, CRM 연동
5.2 공통 통합 모듈 설계
테스트 \& Observability
6.1 유닛/통합 테스트 구조
6.2 로깅·메트릭·트레이싱 연동
8. 프론트엔드(Next.js PWA) 설계·구현 가이드
프론트엔드 아키텍처​
Next.js 구조
2.1 app router, layout, route group 설계
2.2 국제화, SEO, PWA 설정
상태·데이터 패턴
3.1 RSC vs Client Components
3.2 TanStack Query 또는 SWR 정책
UI 컴포넌트 시스템
4.1 shadcn/ui 기반 디자인 시스템
4.2 Tailwind 유틸 규칙
4.3 컴포넌트 트리·스토리북 구성
워크플로우 에디터 구현
5.1 노드 그래프 UI, 드래그·줌·선 연결
5.2 속성 패널, 데이터 미리보기, 실행 컨트롤
성능·접근성 최적화
9. ESP(메일 발송 시스템) 연동 \& AB 테스트 가이드
ESP 선택·아키텍처
템플릿·세그먼트 설계
Webhook/Events 처리 워크플로우
A/B 테스트 프레임워크
4.1 실험 설계
4.2 지표·기간·분석
법적·스팸 정책 고려(Opt-in/Opt-out, Footer 등)
10. Observability/로깅/평가/거버넌스 가이드
Observability 개요​
로깅 전략(구조화, PII 분리)
메트릭·알람 설계
3.1 성공률, 지연, 오류 분류, LLM 비용
트레이싱(분산 트레이싱)
AI 품질 평가·피드백 루프
5.1 유저 피드백 수집
5.2 자동·수동 평가
AI 거버넌스
6.1 프롬프트/모델 변경 관리
6.2 사용 정책·리스크 리뷰 프로세스
11. 배포·운영·CI/CD \& 비용 최적화 가이드
배포 전략(환경·리전)​
Monorepo CI/CD 파이프라인
2.1 빌드 캐시, 테스트 단계, 프론트/백 분리 배포
인프라 as Code
비용 모니터링 \& 최적화
4.1 LLM 호출·스토리지·트래픽 비용
4.2 FinOps 대시보드·알람
롤백·릴리즈 전략
12. 운영 Runbook \& 확장(고도화) 시나리오 가이드
Runbook 개요
장애 유형별 대응 플로우
2.1 API 장애, LLM 장애, DB 장애, 외부 통합 장애
인시던트 관리 프로세스
확장 시나리오
4.1 기능 확장 (새 워크플로우/노드)
4.2 성능 확장(멀티리전·샤딩·캐싱)
4.3 조직 확장(엔터프라이즈 플랜, 멀티테넌시)
이 목차 세트를 기반으로 각 .md를 작성하면, “기획 → 도메인 → 에이전트 → 데이터/RAG → LLM/프롬프트 → 워크플로우 → 백/프론트 → ESP → Observability → 배포/운영 → Runbook”까지 전체 라이프사이클을 바이브 코딩 친화적으로 완전히 덮을 수 있습니다.

질문에 추가된 세 가지 축을 반영해서, 기존 설계에 무엇을 어떻게 더해야 완전해지는지만 딱 짚어 정리하겠습니다.[wikidocs+2](https://wikidocs.net/267810)​

1. Relevance Checker 모듈 편입: 어디에 넣을 것인가
관련성 체커(Relevance Checker)는 **RAG + LangGraph 워크플로우의 “검색 결과 검증 루프”**입니다.[wikidocs](https://wikidocs.net/267810)​
편입 위치
디렉터리 3의 **04-data-rag-infra.md**와 **06-service-workflows-and-langgraph.md**에 다음 챕터를 추가합니다.
04-data-rag-infra.md에 추가
“4.x 관련성 체커(Relevance Checker) 모듈”
역할:
question, context를 입력받아 “이 context가 질문에 실제로 관련 있는가?”를 yes/no 또는 score로 평가.[wikidocs](https://wikidocs.net/267810)​
구현 패턴:
LangChain Runnable/Chain으로 question_answer_relevant 정의
프롬프트 예시(groundedness / relevance 체크용 템플릿)
설정 항목:
기준 임계값(threshold), 재검색 회수 제한, 로그/모니터링(얼마나 자주 no가 나오는지).[wikidocs](https://wikidocs.net/267810)​
06-service-workflows-and-langgraph.md에 추가
“3.x Relevance Check 라우팅 패턴”
retrieve → relevance_check → (yes → llm_answer, no → retrieve) 구조를 LangGraph 예제로 포함.[wikidocs](https://wikidocs.net/267810)​
GraphState에 question, context, relevance 필드 정의, is_relevant 라우터 함수와 재귀 한도(recursion_limit) 설정을 예시로 명시.[swarnendu+1](https://www.swarnendu.de/blog/langgraph-best-practices/)​
GraphRecursionError 방지 전략(재시도 횟수, fallback 응답 정책)까지 포함.
2. OpenRouter + LangChain + LangGraph 혼합: 아키텍처·가이드 반영
2-1. OpenRouter 기반 LLM 인프라
다음 문서에 OpenRouter 전용 챕터를 추가합니다.
05-llm-and-prompt-engineering.md
“2.x LLM Provider 전략 – OpenRouter 중심”
OpenRouter를 기본 LLM 게이트웨이로 두고, 모델 선택을 config 기반으로 하는 구조.[peliqan](https://peliqan.io/blog/langchain-vs-langgraph/)​
장점: 다수 모델 / 비용 최적화 / 지역 제약 우회.
구현 가이드:
LangChain에서 OpenRouter Chat 모델 래퍼 사용
모델 이름·max_tokens·temperature를 환경변수로 주입.
monorepo-structure-and-env.md
OpenRouter 관련 환경변수: OPENROUTER_API_KEY, OPENROUTER_BASE_URL, 모델 기본값.
환경별(Dev/Stage/Prod) 다른 모델/가격대 구성.
2-2. LangChain + LangGraph 혼합 패턴
아키텍처 상에서 제1원칙은 **“LangChain은 빌딩블록, LangGraph는 오케스트레이션 런타임”**입니다.[freecodecamp+1](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)​
03-multi-agent-architecture.md
“3.x LangChain 컴포넌트 재사용 전략”
Retriever, PromptTemplate, Tool, Chains는 LangChain으로 정의.
이들을 LangGraph의 Node 함수 안에서 호출하는 패턴 정리.[peliqan+1](https://peliqan.io/blog/langchain-vs-langgraph/)​
예:
pdf_retriever = … (LangChain)
def retrieve(state: GraphState): retriever.invoke(state["question"]) (LangGraph node).[freecodecamp+1](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)​
06-service-workflows-and-langgraph.md
“4.x LangChain → LangGraph 마이그레이션 체크리스트”[peliqan](https://peliqan.io/blog/langchain-vs-langgraph/)​
1단계: LangChain으로 체인/RAG/프롬프트 검증
2단계: 검증된 컴포넌트를 LangGraph 노드로 감싸 그래프로 조립
3단계: 상태/체크포인트/에러 핸들링 추가.
3. 5가지 role(system / user / assistant / developer / tool) 프롬프트 가이드 추가
바이브 코딩을 안정적으로 쓰려면, 메시지 role별 책임을 정교하게 분리해야 합니다.youtube​[reddit+1](https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/)​
3-1. 전용 가이드북 챕터
05-llm-and-prompt-engineering.md에 아래 챕터 추가:
“3. 메시지 역할(role)별 프롬프트 설계”
(1) developer (구 system) 역할
목적: 모델의 장기적 행동 규칙, 스타일, 금칙사항, 도메인 정책 정의.[reddit+2](https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/)​
특징:
가장 높은 우선순위, 잘 변하지 않는 “헌법/규칙서”에 가까운 내용.
예:
“너는 글로벌 워크플로우 빌더 SaaS의 아키텍트 어시스턴트이다. 항상 보안·비용·거버넌스를 고려해 답한다.”
“프롬프트 예시는 JSON 코드블록으로만 답하고, 한국어 설명을 함께 제공한다.”
(2) system 역할
목적: 런타임 컨텍스트·툴 응답·상태 요약 제공.[reddit](https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/)​
예:
이전 대화 요약, 현재 워크플로우 상태, 관련성 체크 결과(예: “현재 검색 결과는 질문과의 관련성이 낮음”)를 system 메시지로 공급.
Tool 호출 결과를 system으로 제공해 모델이 “이건 도구가 준 정보”임을 알게 하는 패턴.[reddit](https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/)​
(3) user 역할
목적: 인간 사용자의 의도·요구사항·질문·명령 전달.[openai](https://community.openai.com/t/prompts-for-system-assistant-roles/85605)​youtube​
바이브 코딩용 user 패턴:
“이런 기능을 가진 글로벌 서비스 화면을 설계해줘”,
“아래 요구사항을 만족하는 LangGraph 그래프 정의 코드를 생성해줘” 등.
(4) assistant 역할
목적: LLM 응답을 표현하는 채널; 모델이 만든 코드·설계·설명을 여기에 기록.youtube​[openai](https://community.openai.com/t/prompts-for-system-assistant-roles/85605)​
전략:
assistant 응답 중 일부를 다시 system 또는 developer로 승격시켜 “새로운 규칙/패턴”으로 재사용하는 메커니즘도 포함(예: 프롬프트 라이브러리 업데이트).[swarnendu](https://www.swarnendu.de/blog/langgraph-best-practices/)​
(5) tool 역할
목적: 외부 도구 호출·결과를 표현하는 전용 역할.youtube​
예:
LangChain의 Tools, LangGraph ToolNode, n8n HTTP Request 결과 등을 tool 메시지로 싱크.
모델이 “지금은 내 추론이 아니라 도구 결과를 읽는 단계”임을 명확히 알도록 설계.
3-2. 역할별 템플릿·모듈화
동일 문서에 다음 섹션을 추가:
“3.x 역할별 프롬프트 템플릿 모듈”
/prompts/developer/*.md: 제품 전역 규칙, 보안/거버넌스, 톤/스타일.
/prompts/system/*.md: 각 워크플로우/에이전트별 상태·컨텍스트 요약 템플릿.
/prompts/user/*.md: 기획/설계/코드 생성/리팩토링/테스트용 바이브 코딩 유저 프롬프트 템플릿.
/prompts/tool/*.md: 도구 응답 포맷, LLM이 해석하기 쉬운 JSON 스키마.[danbibibi.tistory+1](https://danbibibi.tistory.com/321)​
4. 전체 설계에 대한 “누락 여부” 점검 요약
질문에서 추가하신 요구까지 반영하면, 다음이 모두 커버됩니다.
Relevance Checker 모듈: RAG/워크플로우/에이전트 레벨에서의 관련성·Groundedness 검증 + 재검색 루프.[wikidocs](https://wikidocs.net/267810)​
OpenRouter 기반 LLM 인프라: 비용·모델 선택 전략, LangChain 래퍼, 환경변수 설계.[peliqan](https://peliqan.io/blog/langchain-vs-langgraph/)​
LangChain + LangGraph 혼합 구조: LangChain=컴포넌트, LangGraph=그래프 및 상태·에러 런타임.[freecodecamp+1](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)​
5 role 프롬프트 체계: developer/system/user/assistant/tool 각각의 책임·예시·템플릿 구조.[danbibibi.tistory+1](https://danbibibi.tistory.com/321)​
이 추가 챕터들을 각 가이드북에 삽입하면, 바이브 코딩으로 글로벌 서비스를 설계·생성·운영하는데 필요한 구조적 요소는 빠진 것이 없다고 봐도 될 수준까지 올라갑니다.
[https://wikidocs.net/267810](https://wikidocs.net/267810)
[https://peliqan.io/blog/langchain-vs-langgraph/](https://peliqan.io/blog/langchain-vs-langgraph/)
[https://danbibibi.tistory.com/321](https://danbibibi.tistory.com/321)
[https://www.swarnendu.de/blog/langgraph-best-practices/](https://www.swarnendu.de/blog/langgraph-best-practices/)
[https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)
[https://www.youtube.com/watch?v=xbpdMkTz8L4](https://www.youtube.com/watch?v=xbpdMkTz8L4)
[https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/](https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/)
[https://glasslego.tistory.com/52](https://glasslego.tistory.com/52)
[https://community.openai.com/t/prompts-for-system-assistant-roles/85605](https://community.openai.com/t/prompts-for-system-assistant-roles/85605)
[https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md](https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md)
[https://wikidocs.net/186245](https://wikidocs.net/186245)
[https://wikidocs.net](https://wikidocs.net/)
[https://www.egovframe.go.kr/wiki/doku.php?id=egovframework%3Acompa](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework%3Acompa)
[https://www.kieuns.com/doku.php?id=wiki%3Aplugin-syntax](https://www.kieuns.com/doku.php?id=wiki%3Aplugin-syntax)
[https://github.com/ychoi-kr/wikidocs-chobo-python/actions](https://github.com/ychoi-kr/wikidocs-chobo-python/actions)
[https://www.kieuns.com/wiki:plugin-syntax](https://www.kieuns.com/wiki:plugin-syntax)
[https://blog.langchain.com/building-langgraph/](https://blog.langchain.com/building-langgraph/)
[https://wikidocs.com](https://wikidocs.com/)
[https://atomic.snu.ac.kr/api.php?action=help\&recursivesubmodules=1](https://atomic.snu.ac.kr/api.php?action=help&recursivesubmodules=1)
[https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
[http://wiki1.kr/api.php?action=help\&recursivesubmodules=1](http://wiki1.kr/api.php?action=help&recursivesubmodules=1)

요청하신 수준으로 “모든 내용을 실제 가이드북 전체”로 쓰면, 단일 답변에서 수용 가능한 분량을 훨씬 초과합니다. 그래서 여기서는 **제1원칙 구조를 그대로 유지하면서도, 바로 .md로 복사해 확장 가능한 “완전한 뼈대 + 핵심 문장/예시가 포함된 초안”**까지 제공합니다. 이 틀 위에 챕터별로 세부 내용을 추가하면, 전체 백서 세트를 완성할 수 있습니다.
아래는 1번 가이드부터 12번 가이드까지를 순서대로, 각 문서를 그대로 *.md 파일로 저장해 사용할 수 있는 형태로 정리한 것입니다.

01_vision-requirements.md
비전·요구사항 정의 가이드

1. 서론
목적: 이 문서는 “무엇을 만들 것인가?”를 제1원칙 수준까지 분해해, 모든 설계·구현·바이브 코딩 프롬프트의 기준점을 제공한다.
대상: 경영진, PM, 아키텍트, 리드 엔지니어, UX 리드.
2. 서비스 비전과 성공 지표
2.1 비전·미션
비전: “비개발자도 글로벌 수준의 AI 워크플로우 서비스를 설계·실행할 수 있는 노코드 바이브 코딩 플랫폼을 제공한다.”
미션: “자연어(의도) → 노드 그래프(워크플로우) → 실행 가능한 글로벌 서비스”까지의 거리를 최소화한다.
2.2 North Star Metric
NSM 예: “월간 활성 워크플로우 실행 수(Monthly Active Executions)” 또는 “활성 워크스페이스 당 월간 자동화 작업 수”.
2.3 핵심 KPI
유입: 신규 워크스페이스 생성 수.
활성: 첫 워크플로우를 만들고 실행한 사용자 비율.
유지: 4주 후 재실행 비율.
수익: 유료 플랜 전환률, 워크스페이스 당 ARPA.
3. 시장·경쟁·포지셔닝
3.1 시장
노코드/로우코드 + AI 오케스트레이션 + 멀티에이전트 워크플로우 시장 개요.
글로벌/로컬 경쟁자 맵(Opal, Zapier/Make/n8n, Power Platform, Bubble 등) 요약.
3.2 포지셔닝
“Prompt-to-Workflow + 멀티에이전트 + RAG + 글로벌 UX”가 결합된 플랫폼.
차별점:
바이브 코딩 최적화(프롬프트 템플릿과 아키텍처 가이드 내장).
엔터프라이즈 급 거버넌스·관찰성·FinOps 프레임 포함.
4. 사용자·이해관계자 분석
4.1 페르소나(예)
Growth 마케터, CS 리더, PM, 솔루션 컨설턴트, 엔터프라이즈 IT 관리자.
4.2 내부 이해관계자
운영/지원팀: 알림·로그·권한·리포팅 요구.
영업팀: 데모/PoC를 빠르게 구성하는 템플릿 필요.
5. 기능 요구사항 정의 (What)
5.1 유저스토리
“나는 마케터로서, 신규 리드를 자동 분류·스코어링·후속 이메일 발송 워크플로우를 코드 없이 만들고 싶다.”
“나는 CS 리더로서, 티켓 요약·분류·답장 초안을 자동화하고 싶다.”
5.2 기능 요구사항
워크플로우 에디터(노드·연결·데이터 미리보기).
실행 로그·디버깅·재실행.
멀티에이전트/LLM·RAG 통합.
통합(ESP, Slack, Stripe, CRM 등) 관리.
5.3 워크플로우 관점 요구사항
모든 주요 기능은 “트리거 → 노드 체인 → 결과/알림” 구조로 표현 가능해야 한다.
각 기능은 LangGraph 그래프로도 표현 가능해야 한다.
6. 비기능 요구사항 정의 (How well)
성능: P95 API 응답 ≤ Xms, 워크플로우 실행 지연 ≤ Y초.
가용성: 월 가용성 99.9% 이상(핵심 API 기준).
보안·규제: RBAC, 감사 로그, PII 처리, 데이터 레지던시 고려.
글로벌: 다국어 UI, 타임존 안전성, 통화/날짜 표현.
7. 성공 기준 및 실험 가설
“파일럿 8주 내에, 기존 수동 작업 대비 평균 30% 이상의 시간 절감” 등.
기능별 실험 가설: 예) 관련성 체커 도입 → RAG 응답의 사용자 만족도 +20%.
8. 바이브 코딩 요구사항 표현 템플릿
“다음 요구사항을 만족하는 백엔드/프론트/에이전트/워크플로우 코드를 생성해줘” 템플릿.
프롬프트 구조:
Context(비전, 목표)
Constraints(성능, 보안, 비용, 스택)
Deliverables(파일 구조, 코드 스타일, 테스트 요건)

02_domain-personas-segmentation.md
도메인 모델링 \& 페르소나·세그먼트 설계 가이드

1. 도메인 모델링 원칙
“엔티티·관계·이벤트 수준에서 먼저 정의 → 그 다음 LLM/에이전트/워크플로우에 맵핑.”
RAG·관찰성·과금·권한을 모두 고려.
2. 핵심 엔티티
User, Organization, Workspace, Project
Workflow, Node, Connection, Execution, Log
Template, Integration, Credential, Agent, Dataset, VectorIndex.
각 엔티티에 대해: 필수 필드, 식별자, 수명주기, 권한 범위 정의.
3. 관계 및 이벤트
Workspace ↔ User (역할: Owner/Admin/Member)
Workspace ↔ Workflow (1:N)
Workflow ↔ Execution (1:N)
주요 도메인 이벤트: WorkflowCreated, ExecutionFailed, AgentCostExceeded, RelevanceCheckFailed.
4. 페르소나 및 세그먼트
페르소나별 주요 워크플로우·화면·알림 요구를 표로 정리.

03_multi-agent-architecture.md
멀티에이전트 아키텍처 설계 가이드 (LangGraph)

1. 제1원칙: 왜 에이전트인가
단일 LLM 호출로는 복잡한 다단계 업무(검색→계획→실행→검증)를 안정적으로 처리하기 어렵다.
에이전트 = 역할과 책임이 명확한 LLM + 툴/정책 조합.
2. LangGraph 개념
StateGraph: 상태(메모리)를 가진 그래프 런타임.
노드 = 상태를 읽고/쓰고/도구를 호출하는 함수.
엣지 = 상태/조건에 따른 전이.
3. 에이전트 역할 설계
Planner: 전체 플랜·서브태스크 분해.
Retriever: RAG 검색, 관련성 체커와 연계.
ToolExecutor: API/DB/외부 서비스 호출.
Evaluator/Guardrail: 응답 품질·정책 위반 검사.
4. GraphState 설계
필수 키: question, context, plan, result, cost, steps, errors, relevance_score 등.
5. 패턴별 그래프
Supervisor + Worker 패턴.
Router 패턴(입력에 따라 다른 에이전트 경로 선택).
Reflection 패턴(초안 → 평가 → 수정 루프).

04_data-rag-infra.md
데이터 \& RAG(Qdrant + Supabase) 설계 가이드

1. 데이터 계층 구조
OLTP(Supabase) vs Vector(RAG: Qdrant) vs 로그/메트릭(Observability).
2. Supabase 스키마
워크플로우/실행/사용자/통합/결제 테이블 설계.
3. Qdrant 인덱스
컬렉션: docs, templates, faq, execution_summaries.
벡터 필드, 메타데이터 필드(tenant, language, tags).
4. ETL/동기화 워크플로우
n8n/Opal/LangChain 기반 인덱싱 파이프라인.
5. Relevance Checker 모듈
입력: {question, context_chunk}
출력: {is_relevant: bool, score: float, rationale: str}
LangChain Runnable로 구현, LangGraph에서 노드로 사용.
사용 위치: RAG 단계에서 retrieve → relevance_check → (필터/재검색).

05_llm-and-prompt-engineering.md
LLM 레이어 \& 프롬프트 엔지니어링 가이드

1. LLM 레이어 원칙
모델-불가지론: OpenRouter를 통해 다양한 모델을 사용하되, 인터페이스는 통일.
비용·지연·품질의 균형.
2. OpenRouter 전략
기본 모델 세트: 경량(초안/도우미), 고성능(리포트/복잡 추론)
환경별 설정(Dev=저렴한 모델, Prod=안정 모델).
3. 메시지 역할(role)별 프롬프트 설계
3.1 developer (구 system)
전역 규칙·정책·톤·보안·금칙사항 정의.
문서로 관리, 코드/에이전트 생성 시 항상 포함.
3.2 system
런타임 상태·컨텍스트·툴 결과 요약 제공.
LangGraph의 state/툴 호출 결과를 system에 반영.
3.3 user
실제 사용자·기획자의 의도/요구사항/지시.
바이브 코딩 프롬프트 템플릿.
3.4 assistant
모델 응답 채널, 코드·설계·결과 반환.
3.5 tool
외부 툴/노드/에이전트 결과를 구조화된 JSON으로 표현.
4. 프롬프트 패턴
아키텍처 생성, 컴포넌트/화면 생성, 테스트 코드 생성, 리팩토링, 평가용 템플릿.

06_service-workflows-and-langgraph.md
서비스 Workflow 설계 \& LangGraph 구현 가이드

1. 워크플로우 설계 원칙
모든 기능을 “트리거→노드 체인→결과/알림”으로 표현.
각 노드는 입력/출력/에러/비용을 명확히 정의.
2. 대표 워크플로우 정의
온보딩, 리드 자동화, 리포트 생성, 알림/에러 핸들링.
3. Relevance Check 포함 RAG 워크플로우
Trigger → Retrieve → RelevanceCheck → (관련 없음 → 재검색 / 관련 있음 → LLMAnswer)
LangGraph 노드 코드 스케치.
4. LangGraph 구현
GraphState, 노드 함수, 에지 조건, 체크포인트 설정.

07_fastapi-api-integration.md
백엔드(FastAPI) API \& 통합 가이드
FastAPI 프로젝트 구조, 도메인 모듈, 인증/권한, LangGraph 호출 엔드포인트, 통합 모듈(ESP, Slack, Stripe 등), 로그/메트릭/테스트 패턴.

08_nextjs-pwa-frontend.md
프론트엔드(Next.js PWA) 설계·구현 가이드
app router 구조, 다국어, PWA 세팅, shadcn/ui + Tailwind 컴포넌트 시스템, 워크플로우 에디터 UI, 실행 로그 뷰, 상태 관리 전략.

09_esp-and-ab-test.md
ESP 연동 \& A/B 테스트 가이드
ESP 선택 기준, 템플릿/세그먼트 설계, Webhook 연동, 실험 설계·분석 방법.

10_observability-logging-governance.md
Observability/로깅/평가/거버넌스 가이드
구조화 로깅, 메트릭(워크플로우 성공률·지연·비용), 트레이싱, LLM 품질 평가 루프, AI 거버넌스 프로세스.

11_ci-cd-deployment-cost-optimization.md
배포·운영·CI/CD \& 비용 최적화 가이드
Monorepo 구조(apps/, packages/, infra/), CI 파이프라인, 배포 전략, FinOps(모델 호출·스토리지·트래픽 비용 관리).

12_runbook-and-evolution-scenarios.md
운영 Runbook \& 확장(고도화) 시나리오 가이드
장애 유형별 대응 플로우(LLM 장애, RAG 장애, 외부 통합 장애 등), 인시던트 관리, 확장 시나리오(기능·성능·조직 확장).

이 12개 문서는 이미 **모든 축(서비스 기획, 도메인, 에이전트/LangGraph, RAG+Relevance Checker, OpenRouter+프롬프트 롤, 워크플로우/노드 구조, 백/프론트, ESP, Observability, CI/CD, Runbook)**을 포함하도록 설계되어 있습니다.[wikidocs+3](https://wikidocs.net/267810)​
실제 완성본을 만들고 싶다면:
지금 제안한 각 .md 파일에 대해,
“원칙·목적 문단”
“표/리스트로 된 구체 항목”
“바이브 코딩용 샘플 프롬프트·코드 스케치”
를 채워 넣는 식으로, 한 챕터씩 확장해 나가면 됩니다.
[https://wikidocs.net/267810](https://wikidocs.net/267810)
[https://peliqan.io/blog/langchain-vs-langgraph/](https://peliqan.io/blog/langchain-vs-langgraph/)
[https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)
[https://danbibibi.tistory.com/321](https://danbibibi.tistory.com/321)

지금까지는 12권 각각의 골격과 핵심 챕터를 제시했습니다. 이어서, 바이브 코딩에 실제로 바로 쓸 수 있는 수준으로 각 가이드북에 공통적으로 들어가야 할 “실행 가능한 내용”을 더 구체화하겠습니다.
아래는 각 문서에 공통으로 추가하면 좋은 3가지 레이어입니다.

A. 각 가이드북에 공통으로 추가할 섹션 1: “체크리스트”
각 문서 마지막에 \#\# 체크리스트를 두고, 제1원칙 기준으로 “이게 채워져야 다음 단계로 넘어갈 수 있다”를 명시합니다.
예시 – 01_vision-requirements.md 끝부분:
비전·미션이 한 문장씩 정의되어 있는가?
NSM, 핵심 KPI가 숫자/단위 기준으로 정의되었는가?
주요 페르소나와 각 페르소나별 대표 워크플로우가 문서화되었는가?
기능 요구사항이 유저스토리 형태로 정리되어 있는가?
비기능 요구사항(성능, 보안, 글로벌)이 표 형태로 정리되어 있는가?
“바이브 코딩 요구사항 프롬프트 템플릿”이 최소 3개 이상 준비되었는가?
이 패턴을 02~12번 문서에 동일하게 맞춰서 두면, 문서가 단순 설명서가 아니라 “게이트” 역할을 합니다.

B. 공통 섹션 2: “바이브 코딩용 샘플 프롬프트”
각 가이드북의 마지막 챕터에 \#\# 바이브 코딩 샘플 프롬프트를 추가합니다.
예시 – 05_llm-and-prompt-engineering.md 일부:
developer role 예시:
“너는 글로벌 AI 워크플로우 플랫폼의 아키텍트 어시스턴트이다. 아래 정책을 항상 따른다:
보안과 비용·거버넌스를 최우선으로 고려한다.
워크플로우는 항상 트리거–노드–실행–로깅–에러 처리 구조로 설계한다.
코드 예시는 FastAPI + LangGraph + OpenRouter 조합을 기본으로 한다.
…”
system role 예시:
“현재 사용자는 [마케터] 페르소나이고, 아래와 같은 워크플로우를 이미 보유하고 있다: …
현재 질문: …
최근 RAG 관련성 체커 결과: is_relevant=false 3회 연속 발생.
이 상황을 고려해 답변을 수정하라.”
user role 예시:
“위 비전·요구사항 정의를 기반으로, 멀티에이전트 아키텍처(LangGraph)를 설계하고, 다음 조건을 만족하는 Python 코드 스캐폴드를 생성해줘: …”
각 문서마다 이 식의 프롬프트를 3~5개 넣어두면, **실질적으로 “문서=프롬프트 라이브러리의 구조화 버전”**이 됩니다.

C. 공통 섹션 3: “아티팩트(산출물) 템플릿”
각 가이드북에 \#\# 산출물 템플릿 섹션을 두고, 이 문서를 읽고 나면 최소한 어떤 파일/표/코드가 나와야 하는지 정의합니다.
예시 – 06_service-workflows-and-langgraph.md:
산출물:
workflows/ 폴더에 비즈니스 워크플로우별 .md (시퀀스 다이어그램 + 설명).
graphs/ 폴더에 LangGraph 그래프 정의 코드(*.py) 및 다이어그램 이미지.
“Relevance Checker 포함 RAG 플로우”의 예제 그래프(StateGraph 정의, 노드/엣지, 테스트 케이스).
마찬가지로:
03번 멀티에이전트 가이드는 agents/ 폴더에 역할별 에이전트 정의 파일(설명 + 코드 스켈레톤).
04번 데이터·RAG 가이드는 schemas/, embeddings/, etl/ 폴더에 SQL DDL, 인덱싱 파이프라인 코드 초안.
07/08번 백/프론트 가이드는 apps/api/, apps/web/ 아래 예제 디렉터리 구조와 최소 엔드포인트/페이지 스켈레톤.

다음 단계 제안
이제 구조와 핵심 내용은 모두 잡힌 상태라서, 다음을 바로 하시면 됩니다:
실제 리포 구조 만들기
/docs/01_planning_design/01_vision-requirements.md
/docs/02_workflow_engine/…
/docs/03_service_guides/01~12.md
/docs/04_ux_ui_wireframes/…
위에 정리한 목차·핵심 문장·체크리스트·샘플 프롬프트·산출물 템플릿을 그대로 복사해 초기 버전 작성.
이후에는 가장 우선순위 높은 2~3권부터 세부 내용을 채우면서, 병행해서 그 내용을 그대로 OpenRouter + LangChain + LangGraph에 먹이는 “메타 프롬프트”를 작성하시면 됩니다.
예: vision-requirements.md를 context로 주고, “여기에 맞는 LangGraph 스캐폴드 생성” 같은 식.
원하시면, 다음 턴에서 특정 가이드북 하나(예: 05 LLM/프롬프트 가이드 또는 06 워크플로우 \& LangGraph 가이드)를 골라 실제 본문까지 꽤 자세하게 써 드릴 수 있습니다.

내용을 단계별로 하나하나 심층분석 합니다. 그리고 제1원칙사고에 기준하여 분류하고 모든 내용이 포함되도록 총 5개의 디렉토리 구조에 세분화하여 목차 세트를 새롭게 정리합니다. 세분화 작업은 목차세트를 정리한 후에 다음턴에서 하겠습니다.

요청 내용을 제1원칙 기준으로 재구성하면, 문서 세트는 **“수명주기 + 추론 스택 + 실행 스택 + 운영 스택 + 인터랙션(UX/프롬프트) 스택”** 5축으로 분리하는 것이 가장 깔끔합니다.[^1][^2][^3][^4]

아래는 이를 반영한 **5개 디렉터리 · 통합 목차 세트(상세)**입니다.

***

## 디렉터리 1: Product \& Domain Blueprint (`/01_product_domain`)

> “무엇을, 누구를 위해, 어떤 제약 하에 만드는가”를 정의하는 레이어.[^5][^1]

### 1-1. 비전·요구사항·가치 제안

- `vision-and-goals.md`
    - 서비스 비전/미션
    - North Star Metric, 핵심 KPI 세트
    - 핵심 가치 제안(USP), 성공 기준(출시/1년 차)
- `requirements-functional-nonfunctional.md`
    - 기능 요구사항: 유저스토리, Use Case, MoSCoW 우선순위
    - 비기능 요구사항: 성능, 확장성, 가용성, 보안/규제, 국제화/접근성
- `stakeholders-and-use-cases.md`
    - 외부 사용자·내부 이해관계자·그림형 Use Case 맵
    - 기능별 책임(RACI) 개요


### 1-2. 도메인 모델 \& 세그먼트

- `personas-and-segments.md`
    - 주요 페르소나(마케터, CS 리더, PM, IT 관리자 등)
    - 세그먼트(규모, 산업, 지역/언어, 플랜 유형)와 목표 워크플로우
- `domain-modeling.md`
    - 핵심 엔티티: User, Org, Workspace, Project, Workflow, Node, Execution, Log, Template, Integration, Credential, Agent, Dataset, VectorIndex 등
    - 관계/제약(ERD 수준), 데이터 라이프사이클 정의
- `domain-events-and-triggers.md`
    - 도메인 이벤트 카탈로그 (NewLeadCreated, CampaignFinished 등)
    - 이벤트 ↔ 워크플로우 트리거 매핑


### 1-3. 정보 구조 \& 화면 수준 구조

- `information-architecture.md`
    - IA: 메뉴, 네비게이션, 정보 계층(Workspace > Project > Workflow > Execution)
    - URL 전략(언어 코드, 리전, 다국어 URL 패턴)
- `screens-and-user-flows.md`
    - 핵심 플로우(온보딩, 대시보드, 워크플로우 편집, 실행 로그, 설정, 결제 등)
    - 각 플로우별 고수준 화면 시퀀스


### 1-4. Product Planning \& Slice 전략

- `development-plan.md`
    - 단계별 마일스톤(PoC → 베타 → GA → 글로벌 롤아웃)
    - Feature slice 전략(세로 슬라이스 기준), 우선순위 맵
- `feature-prd-template.md`
    - 각 기능 단위 PRD 템플릿(목표, 유저스토리, 수용기준, 비기능, 위험요인)[^5]
- `product-checklists.md`
    - “새 기능 추가 시 체크리스트”
    - “릴리즈 전 체크리스트”
    - “AI 기능 위험성 평가 체크리스트”

***

## 디렉터리 2: Architecture \& Execution Engine (`/02_arch_execution`)

> “어떤 기술 스택과 아키텍처로, 어떻게 실행·흐름을 제어할 것인가.”[^6][^7][^8]

### 2-1. 전체 아키텍처 \& 스택

- `tech-stack-and-constraints.md`
    - 프론트: Next.js PWA, shadcn/ui, Tailwind 등
    - 백엔드: FastAPI, LangGraph, LangChain, Supabase, Qdrant
    - 인프라: Vercel/Cloud Run/K8s, CDN, ESP, 모니터링 스택
    - 제약(예산/팀 능력/공급자·리전 제약)
- `architecture-overview.md`
    - C4 컨텍스트/컨테이너/컴포넌트 다이어그램
    - 모놀리식 vs 모듈러 모노레포 vs 마이크로서비스 선택 근거


### 2-2. Workflow · 노드 · 데이터 런타임

- `workflow-concepts-and-layers.md`
    - 레이어: Presentation(에디터) / Workflow Runtime / Nodes / Connections / Data / Credentials / Executions / Debugging[^9][^10]
    - “미니앱 = 그래프(노드/엣지 + 상태)” 개념
- `node-basics.md`
    - 노드 타입: 트리거/액션/코어 로직/서브그래프·에이전트
    - 노드 생명주기(생성→설정→실행→로깅→버전)
- `node-catalog.md`
    - 기능별 노드 카탈로그(유저/워크스페이스, 통합, AI/RAG, 유틸리티)
    - 각 노드의 입력/출력 스키마, 옵션, 실패 시 동작
- `connections-and-flow-control.md`
    - 단일/병렬/브랜치/합류 패턴
    - 순서 결정, 의존성, 멱등성 고려
    - LangGraph StateGraph와의 매핑[^7][^6]
- `data-model-in-workflows.md`
    - 워크플로우 내 데이터 구조(items[], JSON, 멀티모달)
    - 변환·검증 규칙, 에러 처리, 타입 전략


### 2-3. Credentials \& Secrets · 실행 \& 디버깅

- `credentials-and-secrets.md`
    - API 키/OAuth/서비스 계정 모델, 암호화 저장, 로테이션
    - 워크플로우에서의 스코프·권한 최소화[^11][^12]
- `executions-and-logging.md`
    - 실행(run) 모델, 상태(대기/성공/실패), 리트라이 정책
    - 실행 로그 구조(노드별 입력/출력/에러/메트릭)
- `debugging-and-data-pinning.md`
    - 데이터 핀닝·모킹 개념과 사용 가이드
    - 에러 패턴(JSON, Expression, 타임아웃 등)별 디버깅 레시피[^13][^14]


### 2-4. LangChain + LangGraph · Prompt-to-Graph

- `langchain-langgraph-integration.md`
    - 제1원칙: LangChain=컴포넌트(Chain/Tool/Retriever), LangGraph=오케스트레이터[^8][^15]
    - LangChain 객체를 LangGraph 노드에서 호출하는 패턴
- `prompt-to-graph-strategy.md`
    - 자연어 → 노드 그래프 생성(PTG/Opal/자체 도구) 전략
    - 그래프 품질 체크리스트(루프, 에러 경로, 자격 증명, 비용)[^16][^17]

***

## 디렉터리 3: LLM · RAG · Agentic Layer (`/03_llm_rag_agents`)

> “LLM·RAG·에이전트가 어떻게 협업하고, 비용·품질을 어떻게 관리하는가.”[^15][^6][^8]

### 3-1. LLM Provider \& OpenRouter 전략

- `llm-provider-strategy-openrouter.md`
    - OpenRouter 중심 모델 전략(저비용/고품질 모델 조합)[^8]
    - 환경별 기본 모델·fallback 모델, rate limit·비용 가드
- `llm-layer-architecture.md`
    - LLM 호출 레이어(공통 wrapper, 로깅, 재시도, 백오프)
    - 동기/비동기 호출 패턴, 스트리밍 전략


### 3-2. 프롬프트 아키텍처 \& Role 체계

- `prompt-roles-and-instruction-hierarchy.md`
    - developer/system/user/assistant/tool 역할 정의와 우선순위[^18][^19][^20]
    - 역할별에 어떤 내용이 들어가야/들어가면 안 되는지
- `prompt-templates-and-patterns.md`
    - 아키텍처 생성 / 컴포넌트 생성 / 테스트 생성 / 리팩토링 / 평가 패턴[^21][^22][^23]
    - Role별 메시지 셋 예시(바이브 코딩용 세트)
- `prompt-library-structure.md`
    - `/prompts/developer/`, `/prompts/system/`, `/prompts/user/`, `/prompts/tool/` 디렉터리 설계[^24][^4]
    - 버전 관리·실험(A/B) 방법


### 3-3. 멀티에이전트 아키텍처 (LangGraph)

- `multi-agent-architecture.md`
    - 에이전트 역할: Planner, Retriever, Coder, Evaluator, Router 등[^25][^6]
    - GraphState 설계(키, 타입, reducer 패턴)
- `agent-patterns-and-best-practices.md`
    - Supervisor/Worker, Router, Reflection 패턴[^26][^6]
    - 루프·비용 폭주 방지, 실패·fallback 전략


### 3-4. 데이터 \& RAG · Relevance Checker

- `data-rag-infra.md`
    - Supabase 스키마, Qdrant 컬렉션, 인덱싱 파이프라인[^15]
    - ETL(배치/스트리밍), 데이터 등급·보안
- `relevance-checker-module.md`
    - Relevance Checker 역할/입출력/스코어링 구조[^27]
    - LangChain Runnable 구현·프롬프트 예시
    - LangGraph 라우팅 패턴 (retrieve → relevance_check → 재검색/생성)[^6]
- `rag-agent-integration-patterns.md`
    - Retrieval → Relevance → Planning → Generation
    - 품질 평가 루프(질문-문맥-응답 평가 데이터 저장)

***

## 디렉터리 4: Delivery Stack (Backend · Frontend · DevOps) (`/04_delivery_stack`)

> “API, 프론트, 배포/운영으로 실제 사용자에게 가는 경로.”[^28][^29][^30]

### 4-1. 백엔드(FastAPI) \& 통합

- `fastapi-architecture.md`
    - 모듈/레이어 구조(라우터, 서비스, 리포지토리, 스키마)
    - 도메인별 API 설계(워크플로우/실행/로그/통합 등)
- `langgraph-backend-integration.md`
    - LangGraph 실행을 위한 엔드포인트 패턴(sync/async)[^26]
    - 백그라운드 작업/큐 사용 여부, 체크포인트/재실행 설계
- `external-integrations.md`
    - ESP, Slack, Stripe, CRM 연동 패턴
    - 공통 통합 모듈, 에러 핸들링, 재시도·멱등성


### 4-2. 프론트엔드(Next.js PWA)

- `nextjs-architecture.md`
    - app router 구조, layout/route group, 국제화/SEO/PWA[^29][^31]
- `state-and-data-fetching.md`
    - RSC vs Client Component 전략
    - TanStack Query/SWR 페치 패턴, 캐싱·에러 처리
- `workflow-editor-ui.md`
    - 노드 그래프 UI, 드래그·줌·연결 인터랙션
    - 속성 패널, 실행 로그/상태 표시 UI


### 4-3. DevOps · CI/CD · Monorepo

- `monorepo-structure-and-env.md`
    - `apps/`(web/api/worker), `packages/`(ui/core/llm/rag), `infra/` 구조[^30][^29]
    - env/secret 관리(.env, Vault, CI secrets), 환경별 설정
- `ci-cd-pipelines.md`
    - 빌드/테스트/배포 파이프라인(프론트·백 분리, 캐시 전략)
    - Dev/Stage/Prod, Canary/Blue-Green, 롤백 정책
- `deployment-and-cost-optimization.md`
    - 인프라 as Code, 리소스 스케일링
    - LLM·스토리지·트래픽 비용 모니터링 및 최적화[^32]

***

## 디렉터리 5: UX · Interaction · Ops Runbook (`/05_ux_interaction_ops`)

> “사람과 시스템의 상호작용, 프롬프트 UX, 관찰성, 운영 Runbook.”[^2][^3][^21]

### 5-1. UX 원칙 · 화면 설계

- `ux-principles-and-navigation.md`
    - 글로벌 UX 원칙(일관성/피드백/오류 복구/접근성)
    - 네비게이션 모델(대시보드/에디터/설정/리포트 모드)
- `wireframes-dashboard.md`
    - 로그인 후 대시보드 레이아웃·컴포넌트 트리·상태/이벤트
- `wireframes-workflow-editor.md`
    - 캔버스/노드 목록/속성 패널/실행 로그/버전 히스토리 구역
    - shadcn/ui·Tailwind 매핑, 상태/이벤트 정의
- `wireframes-execution-and-debugging.md`
    - 실행 이력·타임라인·노드별 입출력·재실행 버튼 UI
- `wireframes-settings-and-integrations.md`
    - Workspace/멤버/권한/통합 설정 화면 구조


### 5-2. Prompt UX \& Vibe Coding Playbook

- `vibe-coding-workflow.md`
    - “Describe → Plan → Scaffold → Refine → Test → Document” 루프[^3][^33][^21]
- `prompt-ux-patterns.md`
    - 사용자에게 어떤 정보(맥락·제약·예시)를 요구할지 UX 관점 정의
    - 에러/부정확 답변 시 재프롬프트 UX 패턴
- `prompt-playbooks.md`
    - “아키텍처 리뷰 요청용 프롬프트”
    - “코드 리팩토링 요청용 프롬프트”
    - “버그 재현/추적 프롬프트”[^4][^24]


### 5-3. Observability · 거버넌스 · Runbook

- `observability-and-logging.md`
    - 구조화 로그, 메트릭(성공률·지연·비용), 분산 트레이싱[^2]
- `ai-evaluation-and-feedback-loops.md`
    - 유저 피드백 수집, 자동/수동 평가, 품질 리포트
- `ai-governance-and-risk.md`
    - 프롬프트/모델 변경 관리, 정책·리스크 리뷰 프로세스[^19][^20]
- `operations-runbook.md`
    - 장애 유형별(LLM, RAG, DB, 외부 통합) 대응 플로우
    - 인시던트 프로세스, 에스컬레이션, 커뮤니케이션 템플릿
- `evolution-scenarios.md`
    - 기능 확장, 성능 확장(멀티리전·캐싱), 조직 확장(멀티테넌시·엔터프라이즈)

***

이 구조는:

- 디렉터리 1: Product/도메인(What, For whom)
- 디렉터리 2: 아키텍처·워크플로우 런타임(How it flows)
- 디렉터리 3: LLM/RAG/에이전트(Thinking layer)
- 디렉터리 4: 백·프론트·DevOps(Delivery layer)
- 디렉터리 5: UX/프롬프트/운영(Interaction \& Operations)

로 분리되어, 바이브 코딩으로 설계→구현→운영→확장을 수행하는 데 필요한 모든 층을 빠짐없이 포함합니다.[^1][^3][^4][^6]

다음 턴에서 원하시면, 이 5개 디렉터리 중 하나를 선택해 **각 .md 파일의 세부 섹션/문단 수준까지 더 쪼개는 “세분화 작업”**을 이어가겠습니다.
<span style="display:none">[^34][^35][^36][^37]</span>

<div align="center">⁂</div>

[^1]: https://dev.to/wasp/a-structured-workflow-for-vibe-coding-full-stack-apps-352l

[^2]: https://docs.vibe-coding-framework.com/documentation-standards

[^3]: https://cloud.google.com/discover/what-is-vibe-coding

[^4]: https://github.com/cpjet64/vibecoding/blob/main/system-architecture-guide.md

[^5]: https://www.linkedin.com/pulse/how-create-better-apps-my-7-step-vibe-coding-workflow-szerovay-0aqcf

[^6]: https://www.swarnendu.de/blog/langgraph-best-practices/

[^7]: https://www.langchain.com/langgraph

[^8]: https://peliqan.io/blog/langchain-vs-langgraph/

[^9]: https://docs.n8n.io/workflows/

[^10]: https://deepwiki.com/n8n-io/n8n-docs/2.1-workflows-and-data-flow

[^11]: https://docs.n8n.io/integrations/builtin/credentials/

[^12]: https://www.reco.ai/hub/secure-n8n-workflows

[^13]: https://docs.n8n.io/data/data-pinning/

[^14]: https://docs.n8n.io/data/data-mocking/

[^15]: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/

[^16]: https://github.com/langchain-ai/langgraph/issues/3365

[^17]: https://github.com/langchain-ai/langgraph/discussions/3363

[^18]: https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case/leveraging-system-user-and-assistant-roles-for-better-prompts

[^19]: https://www.clarifai.com/blog/agentic-prompt-engineering

[^20]: https://practiqai.com/blog/system-prompts-roles-instruction-hierarchy

[^21]: https://vibecoding.app/blog/how-vibe-coding-works

[^22]: https://zread.ai/tukuaiai/vibe-coding-cn/2-quick-start

[^23]: https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md

[^24]: https://roboco.io/posts/vibe-coding-manual/

[^25]: https://langchain-ai.github.io/langgraph/concepts/multi_agent/

[^26]: https://blog.langchain.com/building-langgraph/

[^27]: https://wikidocs.net/267810

[^28]: https://forum.cursor.com/t/best-practices-for-structuring-a-next-js-fastapi-supabase-project/49706

[^29]: https://www.pronextjs.dev/workshops/next-js-react-server-component-rsc-architecture-jbvxk/understanding-the-example-monorepo-structure-4gpny

[^30]: https://github.com/belgattitude/nextjs-monorepo-example/blob/main/README.md

[^31]: https://elementor.com/blog/what-is-n8n/

[^32]: https://buymeacoffee.com/afgarabote/building-modern-full-stack-applications-next-js-fastapi-supabase-vercel

[^33]: https://emergent.sh/learn/what-is-vibe-coding

[^34]: https://velog.io/@gyu_p/%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4-%EC%95%88%ED%95%B4%EB%8F%84-%EC%9E%98-%EB%90%98%EB%8D%98%EB%8D%B0

[^35]: https://github.com/langchain-ai/langgraph/discussions/2090

[^36]: https://docs.nvidia.com/nim/large-language-models/latest/system-example.html

[^37]: https://awslabs.github.io/mcp/vibe_coding

