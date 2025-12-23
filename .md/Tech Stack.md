Tech Stack

***

## 1. 언어 · 런타임

- 필수  
  - Python 3.10+ (에이전트, LangGraph, RAG, 백엔드)
  - TypeScript 5+ (Next.js 프론트엔드)
- 옵션  
  - Node.js 20+ (유틸 스크립트, 프론트 빌드)  

***

## 2. Agentic · LLM · RAG 레이어

- 오케스트레이션  
  - LangGraph (Python) – 멀티에이전트 워크플로우, StateGraph
  - LangChain Core – LLM/Tool/Retriever 컴포넌트

- LLM Provider · Gateway  
  - OpenRouter – 멀티 모델 게이트웨이 (GPT-4.1, 4.1-mini, Claude, o3 등)
  - (옵션) Portkey / Helicone – 비용·레이튼시·로깅이 필요한 경우

- 임베딩 & RAG 도구  
  - OpenAI text-embedding-3-large (임베딩)
  - Qdrant 또는 Pinecone (Vector DB)
  - pdfplumber, PyMuPDF (PDF 추출)  

---

## 3. 백엔드 · 인프라

- 웹 API  
  - FastAPI – LangGraph 위에 API 레이어 구성
  - (옵션) LangServe – LangChain/LangGraph용 서버 래퍼

- 데이터베이스  
  - Supabase (Postgres + Auth + Storage)  
  - (옵션) Redis – 큐/세션/캐시  

- 배포/실행 환경  
  - Docker +  
    - Google Cloud Run / AWS ECS / Kubernetes 중 택1
  - (프론트) Vercel – Next.js 호스팅

***

## 4. 프론트엔드 · UX

- 프레임워크  
  - Next.js 14 (App Router, RSC, PWA)

- 상태·데이터  
  - TanStack Query – 서버 데이터 패칭/캐싱
  - (옵션) Zustand – 가벼운 전역 상태  

- UI 컴포넌트  
  - shadcn/ui + Tailwind CSS – 대시보드/에디터 UI
  - react-markdown – 챕터 초안 렌더링  

***

## 5. Observability · 평가 · 거버넌스

- 로깅/트레이싱  
  - OpenTelemetry SDK (Python·Node)
  - 중앙 수집: Prometheus + Grafana 또는 Datadog/New Relic

- LLM Observability  
  - LangSmith (LangChain/LangGraph 네이티브)
  - (오픈소스 대안) Langfuse / Phoenix / TruLens

- 평가/가드레일  
  - TruLens 또는 Phoenix – RAG 품질·드리프트 모니터링
  - 자체 AgentEval 파이프라인 (LangGraph + LLM)  

***

## 6. DevOps · 협업 도구

- 버전 관리 · CI/CD  
  - GitHub + GitHub Actions (빌드/테스트/배포)
  - (옵션) GitLab CI, CircleCI  

- IaC  
  - Terraform or Pulumi – GCP/AWS 인프라 정의

- 협업  
  - Cursor / VS Code (+ Copilot 류) – 바이브 코딩 환경
  - Notion / Obsidian – 설계·PRD·Runbook 관리  

이 구성을 그대로 BAAS 기본 스택으로 두고, 이후에는 “어떤 계층(LLM·RAG·LangGraph·API·프론트·Ops)을 작업하는지”에 따라 위 도구들 중 해당 부분만 세부적으로 사용하면 됩니다.