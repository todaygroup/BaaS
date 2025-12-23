# 프로젝트 모노레포 스캐폴드 (Project Monorepo Scaffold)

이 문서는 BAAS의 실제 구현을 위한 최종 모노레포 서비스 디렉터리 구조를 정의합니다. 이 구조는 Guide 1~5에서 논의된 모든 아키텍처 결정을 통합한 최상위 설계도입니다.

---

## 1. 최상위 구조

```text
baas/
├── apps/                  # 실행 가능한 앱들 (웹, API, 워커)
│   ├── web/               # Next.js 프론트엔드
│   ├── api/               # FastAPI + LangGraph 백엔드
│   └── worker/            # 배치 작업, RAG 인덱싱, 장기 그래프 실행
├── packages/              # 공유 라이브러리 (도메인/에이전트/UX 등)
│   ├── core/              # 도메인 모델, 공통 타입/유틸
│   ├── llm_rag/           # LLM Layer + RAG + 에이전트 로직
│   ├── workflows/         # LangGraph 그래프(Book/Chapter/Eval)
│   ├── ui/                # React/shadcn UI 컴포넌트 라이브러리
│   └── prompts/           # 프롬프트 라이브러리 & 메타데이터
├── infra/                 # 인프라/IaC/배포 스크립트
│   ├── terraform/
│   ├── k8s/
│   └── scripts/
├── docs/                  # 백서·가이드북 디렉터리
│   ├── 01_product_domain/
│   ├── 02_arch_execution/
│   ├── 03_llm_rag_agents/
│   ├── 04_delivery_stack/
│   └── 05_ux_interaction_ops/
├── .github/               # CI/CD 워크플로우
├── pyproject.toml         # Python 루트 설정
├── package.json           # JS/TS 워크스페이스 설정
├── turbo.json / nx.json   # 모노레포 빌드/캐시 설정(선택)
└── README.md
```

---

## 2. 세부 디렉터리 구조

### 2.1 apps/api (FastAPI + LangGraph)

```text
apps/api/
├── app/
│   ├── main.py            # FastAPI 엔트리포인트
│   ├── config.py          # 환경 변수/설정
│   ├── deps.py            # DI, 그래프/스토어 주입
│   ├── routes/            # 라우터 (REST API)
│   │   ├── books.py
│   │   ├── chapters.py
│   │   ├── graphs.py      # Book/Chapter/Eval 그래프 실행
│   │   └── exports.py
│   ├── services/          # 비즈니스 로직
│   │   ├── books_service.py
│   │   ├── chapters_service.py
│   │   └── graphs_service.py
│   ├── repositories/      # DB/RAG 접근
│   │   ├── books_repo.py
│   │   ├── chapters_repo.py
│   │   └── executions_repo.py
│   ├── models/            # Pydantic & ORM 모델
│   │   ├── domain_models.py
│   │   └── db_models.py
│   ├── observability/     # 로깅/트레이싱 훅
│   │   ├── logging.py
│   │   └── tracing.py
│   └── workflows/         # packages/workflows 어댑터
│       ├── book_graph_adapter.py
│       └── chapter_graph_adapter.py
└── tests/
```

### 2.2 apps/web (Next.js 프론트엔드)

```text
apps/web/
├── app/
│   ├── layout.tsx
│   ├── page.tsx               # Dashboard
│   ├── workspaces/
│   │   └── [workspaceId]/
│   │       ├── page.tsx       # Project List
│   │       └── projects/
│   │           └── [projectId]/
│   │               ├── page.tsx          # Book List
│   │               └── books/
│   │                   └── [bookId]/
│   │                       ├── page.tsx  # Book Overview
│   │                       ├── chapters/
│   │                       │   └── [chapterId]/page.tsx  # Chapter Workspace
│   │                       └── executions/page.tsx       # Execution List/Detail
├── components/
│   ├── layout/
│   ├── dashboard/
│   ├── book/
│   ├── chapter/
│   ├── executions/
│   └── common/
├── lib/
│   ├── api-client.ts         # FastAPI 호출 래퍼
│   ├── routes.ts             # 경로 헬퍼
│   ├── query-client.ts       # TanStack Query 설정
│   └── config.ts
└── public/
```

### 2.3 apps/worker (배치·RAG·장기 그래프 실행)

```text
apps/worker/
├── worker/
│   ├── main.py               # 엔트리포인트 (Celery/Taskiq/단순 cron)
│   ├── tasks/
│   │   ├── ingest_pdfs.py    # RAG 인덱싱
│   │   ├── reindex.py
│   │   └── scheduled_graphs.py
│   └── config.py
└── tests/
```

### 2.4 packages/core (도메인 모델·유틸)

```text
packages/core/
├── src/
│   ├── domain/
│   │   ├── author.py
│   │   ├── workspace.py
│   │   ├── project.py
│   │   ├── book.py
│   │   ├── chapter.py
│   │   └── execution.py
│   ├── events/
│   │   └── domain_events.py
│   ├── schemas/
│   │   └── api_schemas.py
│   └── utils/
│       └── time.py
└── pyproject.toml
```

### 2.5 packages/llm_rag (LLM · RAG · Agent)

```text
packages/llm_rag/
├── src/
│   ├── llm/
│   │   ├── router.py           # 역할 → 모델 매핑
│   │   ├── client_openrouter.py
│   │   └── layer.py            # 공통 호출/로깅/재시도
│   ├── rag/
│   │   ├── schema.py           # ChunkMetadata
│   │   ├── store.py            # RAGStore 인터페이스
│   │   ├── qdrant_store.py
│   │   ├── ingest_pdf.py
│   │   └── relevance_checker.py
│   ├── agents/
│   │   ├── states.py           # BookState, ChapterState 등
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── chapter_writer.py
│   │   ├── style_agent.py
│   │   └── auto_critic.py
│   └── eval/
│       └── eval_logging.py
└── pyproject.toml
```

### 2.6 packages/workflows (LangGraph 그래프)

```text
packages/workflows/
├── src/
│   ├── book_graph.py          # Book-level Graph 정의
│   ├── chapter_graph.py       # Chapter-level Subgraph
│   ├── eval_graph.py          # Eval Subgraph
│   ├── utils/
│   │   └── observability.py   # run_id/node_id 훅
│   └── langgraph.json         # LangGraph 설정
└── pyproject.toml
```

### 2.7 packages/ui (공통 UI 컴포넌트)

```text
packages/ui/
├── src/
│   ├── components/
│   │   ├── layout/
│   │   ├── cards/
│   │   ├── tables/
│   │   ├── prompts/
│   │   └── charts/
│   └── index.ts
└── package.json
```

### 2.8 packages/prompts (프롬프트 라이브러리)

```text
packages/prompts/
├── developer/
│   └── global_rules.md
├── system/
│   ├── book_context.md
│   └── chapter_context.md
├── user/
│   ├── plan_book.md
│   ├── write_chapter.md
│   └── evaluate_chapter.md
├── tool/
│   └── rag_result_format.md
└── metadata.yml
```

### 2.9 infra (인프라 & 배포)

```text
infra/
├── terraform/           # GCP/AWS 인프라 정의
├── k8s/
│   ├── api-deployment.yaml
│   ├── web-deployment.yaml
│   └── worker-deployment.yaml
└── scripts/
    ├── build_containers.sh
    └── deploy.sh
```
