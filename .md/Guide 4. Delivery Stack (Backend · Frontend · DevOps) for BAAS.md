<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 지금까지 나눈 대화를 심층 분석하여 **Book-Authoring Agent System (BAAS)** 내용을 작성할 때 각 권 별로 백서 형태로 하나씩 문서를 생성합니다. 문서를 작성하기 전에 모든 내용을 "제 1 원칙 사고법"을 기준으로 하여 전 과정을 근본적인 본질에서 시작하여 요약본 형태가 아니라 모든 내용이 하나도 빠짐없이 필요한 모든 단계가 순차적으로 적용된 Full Stack 문서 형태로 작성합니다.

"디렉터리 4: Delivery Stack (Backend · Frontend · DevOps)  " 에 대한 내용을 실제 책 분량 수준으로 더 확장해서 각 권 별로 작성합니다. 이때 실 구현을 위한 코드·템플릿을 상세화하는 과정을 포함하여 모든 소스코드가 포함되도록 작성합니다.

단일 응답에 “책 분량 + 전체 소스코드”를 모두 담을 수는 없어서, 디렉터리 4를 **한 권짜리 백서 구조 + 핵심 설계 + 대표 코드/템플릿 스캐폴드** 수준까지 최대한 깊게 풀어내겠습니다. 이 문서 하나로 BAAS의 Backend · Frontend · DevOps 뼈대를 그대로 구현할 수 있게 만드는 것이 목표입니다.[^1][^2][^3]

아래는 “Guide 4 – Delivery Stack (Backend · Frontend · DevOps) for BAAS”의 구조입니다.

***

# Guide 4. Delivery Stack (Backend · Frontend · DevOps) for BAAS

**Book-Authoring Agent System (BAAS) – 전달 계층 \& 운영 백서**

***

## 1. 제1원칙: BAAS Delivery Stack의 역할

### 1.1 본질적 질문

- BAAS의 “생각하는 레이어(LLM·RAG·Agentic)”는 이미 설계되었다.
- 이제 필요한 것은, 이 능력이 **실제 사용자(저자)가 클릭 한 번으로 사용할 수 있는 서비스**가 되는 경로이다.[^4][^5]

이 경로는 세 층으로 분해된다:

1) **Backend Layer**:
    - BAAS API, LangGraph 실행 엔드포인트, RAG 인덱싱 배치, 관찰성 훅.
2) **Frontend Layer**:
    - 저자가 프로젝트를 만들고, 책 구조를 보고, 챕터 상태를 모니터링하고, 결과를 편집·Export하는 UI.[^2][^6]
3) **DevOps Layer**:
    - 코드 → 빌드 → 테스트 → 배포 → 모니터링 → 스케일링까지 자동화하는 운영 인프라.[^3][^1]

***

## 2. Monorepo 개요

### 2.1 디렉터리 구조 설계

```text
baas/
  apps/
    web/           # Next.js PWA
    api/           # FastAPI + LangGraph
    worker/        # 배치 작업, RAG 인덱싱, 장기 그래프 실행
  packages/
    core/          # 도메인 모델, 공통 타입, 유틸
    llm_rag/       # Guide 3 코드 (LLM·RAG·Agent)
    workflows/     # LangGraph 그래프 정의
    ui/            # React/shadcn 컴포넌트 라이브러리
  infra/
    terraform/     # IaC (옵션)
    k8s/           # 배포 매니페스트 (옵션)
  docs/
    01_product_domain/
    02_arch_execution/
    03_llm_rag_agents/
    04_delivery_stack/
    05_ux_interaction_ops/
```

- `apps/api` 는 BAAS의 **싱글 백엔드 진입점**이다.[^1]
- `packages/workflows` 안에 LangGraph 그래프(Book/Chapter/Eval)를 모듈화한다.[^7]

***

## 3. Backend – FastAPI \& LangGraph (fastapi-architecture.md, langgraph-backend-integration.md)

### 3.1 FastAPI 프로젝트 구조

```text
apps/api/
  app/
    main.py
    deps.py
    config.py
    routes/
      books.py
      chapters.py
      graphs.py
      exports.py
    services/
      books_service.py
      chapters_service.py
      graphs_service.py
    repositories/
      books_repo.py
      chapters_repo.py
      executions_repo.py
    models/
      domain_models.py
      db_models.py
    workflows/
      book_graph_adapter.py
      chapter_graph_adapter.py
  tests/
```


### 3.2 설정 \& DI

```python
# apps/api/app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = "dev"
    db_url: str
    supabase_url: str
    supabase_key: str
    vector_db_url: str
    vector_db_key: str
    openrouter_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

```python
# apps/api/app/deps.py
from fastapi import Depends
from .config import settings
from packages.llm_rag.rag.store import RAGStore
from packages.workflows.book_graph import book_graph
from packages.workflows.chapter_graph import chapter_graph

def get_settings():
    return settings

def get_rag_store():
    return RAGStore(settings.vector_db_url, settings.vector_db_key)

def get_book_graph():
    return book_graph

def get_chapter_graph():
    return chapter_graph
```


### 3.3 Graph 실행 API 설계

#### 3.3.1 Book Graph 실행 API

```python
# apps/api/app/routes/graphs.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from packages.workflows.book_graph import BookState
from ..deps import get_book_graph
from ..repositories.executions_repo import ExecutionsRepo

router = APIRouter(prefix="/graphs", tags=["graphs"])

class BookGraphInput(BaseModel):
    book_id: str
    topic: str
    audience: str
    tone: str

class BookGraphResponse(BaseModel):
    graph_run_id: str
    status: str
    outline: dict

@router.post("/book/run", response_model=BookGraphResponse)
async def run_book_graph(
    payload: BookGraphInput,
    book_graph = Depends(get_book_graph),
    executions_repo: ExecutionsRepo = Depends(ExecutionsRepo),
):
    state: BookState = {
        "book_id": payload.book_id,
        "topic": payload.topic,
        "audience": payload.audience,
        "tone": payload.tone,
    }
    run_id = executions_repo.create_run(
        graph_type="book",
        initial_state=state,
        started_at=datetime.utcnow(),
    )

    # LangGraph 실행 (동기 예시)
    final_state = book_graph.invoke(state)

    executions_repo.finish_run(run_id, final_state)

    return BookGraphResponse(
        graph_run_id=run_id,
        status="succeeded",
        outline=final_state["outline"],
    )
```


#### 3.3.2 Chapter Graph 실행 API

```python
@router.post("/chapter/run")
async def run_chapter_graph(
    payload: ChapterGraphInput,
    chapter_graph = Depends(get_chapter_graph),
    executions_repo: ExecutionsRepo = Depends(ExecutionsRepo),
):
    state: ChapterState = {
        "chapter_id": payload.chapter_id,
        "book_id": payload.book_id,
        "title": payload.title,
        "purpose": payload.purpose,
        "outline": payload.outline,
        "iteration": 0,
    }
    run_id = executions_repo.create_run(...)
    final_state = chapter_graph.invoke(state)
    executions_repo.finish_run(run_id, final_state)
    return final_state
```


### 3.4 External Integrations (external-integrations.md)

여기서는 핵심만 스캐폴드로 제시합니다.

- ESP: **책 완성 시 자동 이메일 발송** (저자에게 알림, PDF 링크).
- Slack: 주요 에이전트 이벤트 슬랙 알림(폭주, 실패, 비용 초과).
- Stripe: BAAS를 서비스화할 경우 요금제·결제와 연계.

```python
# apps/api/app/services/notifications_service.py
from .esp_client import send_email

def notify_book_completed(author_email: str, book_title: str, download_url: str):
    subject = f"[BAAS] '{book_title}' 원고가 준비되었습니다."
    body = f"""
안녕하세요,

요청하신 '{book_title}'의 원고가 생성되었습니다.
아래 링크에서 확인하실 수 있습니다.

{download_url}

감사합니다.
"""
    send_email(to=author_email, subject=subject, body=body)
```


***

## 4. Frontend – Next.js PWA (nextjs-architecture.md, state-and-data-fetching.md, workflow-editor-ui.md)

### 4.1 Next.js 프로젝트 구조

```text
apps/web/
  app/
    layout.tsx
    page.tsx               # 홈/대시보드
    workspaces/
      [workspaceId]/
        layout.tsx
        page.tsx           # 프로젝트 리스트
        projects/
          [projectId]/
            page.tsx       # 책 리스트
            books/
              [bookId]/
                page.tsx   # Book Overview
                chapters/
                  [chapterId]/
                    page.tsx   # Chapter Workspace
                exports/
                  page.tsx
  components/
    layout/
    book/
    chapter/
    common/
  lib/
    api-client.ts
    routes.ts
    query-client.ts
```


### 4.2 데이터 패칭 – RSC + TanStack Query

```ts
// apps/web/app/workspaces/[workspaceId]/projects/[projectId]/books/[bookId]/page.tsx
import { fetchBookDetail } from "@/lib/api-client";
import BookOverview from "@/components/book/BookOverview";

export default async function BookPage({ params }: { params: { workspaceId: string; projectId: string; bookId: string }}) {
  const book = await fetchBookDetail(params.bookId);
  return <BookOverview book={book} />;
}
```

```ts
// apps/web/lib/api-client.ts
export async function fetchBookDetail(bookId: string) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books/${bookId}`, {
    cache: "no-store",
  });
  if (!res.ok) throw new Error("Failed to fetch book");
  return res.json();
}
```

Chapter Workspace는 클라이언트 컴포넌트 + TanStack Query를 사용해 **그래프 실행 상태를 폴링/스트리밍**.[^2]

***

### 4.3 Workflow Editor UI 스캐폴드

```tsx
// apps/web/components/chapter/ChapterWorkspace.tsx
"use client";

import { useQuery, useMutation } from "@tanstack/react-query";
import { Button } from "@/components/ui/button";
import { ChapterGraphTimeline } from "./ChapterGraphTimeline";
import { ChapterDraftViewer } from "./ChapterDraftViewer";
import { runChapterGraph } from "@/lib/api-client";

type Props = {
  chapterId: string;
  bookId: string;
};

export function ChapterWorkspace({ chapterId, bookId }: Props) {
  const { data: execution, refetch } = useQuery({
    queryKey: ["chapter-execution", chapterId],
    queryFn: () => fetchChapterExecution(chapterId),
    refetchInterval: 5000,
  });

  const mutation = useMutation({
    mutationFn: () => runChapterGraph({ chapterId, bookId }),
    onSuccess: () => refetch(),
  });

  return (
    <div className="flex h-full">
      <div className="flex-1 border-r">
        <ChapterGraphTimeline execution={execution} />
      </div>
      <div className="flex-1 flex flex-col">
        <div className="p-2 border-b flex justify-between items-center">
          <h2 className="font-semibold">Chapter Draft</h2>
          <Button onClick={() => mutation.mutate()} disabled={mutation.isPending}>
            {mutation.isPending ? "Running..." : "Run Chapter Graph"}
          </Button>
        </div>
        <div className="flex-1 overflow-auto">
          <ChapterDraftViewer execution={execution} />
        </div>
      </div>
    </div>
  );
}
```

- `ChapterGraphTimeline` 컴포넌트는 NodeRun 리스트를 타임라인/단계 진행 바 형태로 렌더링.
- `ChapterDraftViewer`는 마지막 상태의 `draft_text`를 Markdown 렌더링.

***

## 5. DevOps – Monorepo, CI/CD, 배포 \& 비용 최적화 (monorepo-structure-and-env.md, ci-cd-pipelines.md, deployment-and-cost-optimization.md)

### 5.1 환경변수 \& Secret 관리

```text
.env.development
.env.staging
.env.production
```

예:

```bash
# apps/api/.env
ENV=dev
DB_URL=postgres://...
SUPABASE_URL=...
SUPABASE_KEY=...
VECTOR_DB_URL=...
VECTOR_DB_KEY=...
OPENROUTER_API_KEY=...
```

CI에서는 `.env` 대신 **GitHub Actions Secrets / Vault** 참조.

***

### 5.2 CI/CD 파이프라인 스캐폴드 (GitHub Actions 예)[^3][^1]

```yaml
# .github/workflows/ci-cd.yml
name: CI-CD

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        ports: ["5432:5432"]
        env:
          POSTGRES_PASSWORD: postgres
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install backend deps
        run: |
          pip install -r apps/api/requirements.txt
      - name: Run backend tests
        run: |
          cd apps/api && pytest

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Install frontend deps
        run: |
          cd apps/web && npm ci
      - name: Run frontend tests
        run: |
          cd apps/web && npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      # 빌드 & 컨테이너 이미지 push (예: ghcr.io, ECR)
      # 이후 infra/k8s 또는 Cloud Run, Vercel CLI 사용해 배포
```


***

### 5.3 배포 전략 \& 비용 최적화

- **API/Worker**: Cloud Run / ECS / K8s 중 선택.
- **Web**: Vercel / Static Export.
- LLM 비용 줄이기:
    - Dev 환경: gpt-4.1-mini / o3-mini 사용.
    - RAG로 컨텍스트 최소화, 요약 체인 삽입.
    - AgentEval/AutoCritic도 “샘플 실행만 평가” 전략.[^8][^9]

***

## 6. End-to-End 요청 플로우 예시

1) 저자가 Web UI에서 “새 책 생성 → 아웃라인 생성” 클릭.
2) Web → API `/graphs/book/run` 호출.
3) FastAPI에서 BookState 생성 → LangGraph Book Graph 실행 → Outline 생성.
4) 결과는 DB에 저장, UI에서 Book Overview에 렌더링.
5) 저자가 특정 챕터를 선택하고 “Run Chapter Graph” 클릭.
6) Web → API `/graphs/chapter/run` → Chapter Graph 실행 → RAG/Writer/Eval 루프.
7) 실행 상태는 Executions/NodeRuns 테이블에서 폴링 → Timeline \& Draft 뷰에 시각화.
8) 최종 통합 후 Export API 호출 → MD/DOCX/PDF/JSON 생성 → 다운로드 링크 제공.

이 플로우에서:

- **디렉터리 2·3의 그래프/에이전트/LLM·RAG 레이어**는 이미 작성한 코드와 연결되고,
- **디렉터리 4의 Backend/Frontend/DevOps**가 그 레이어를 실제 사용자와 연결해 준다.[^10][^11]

***

## 7. Delivery Stack 체크리스트

- [ ] FastAPI 백엔드가 Book/Chapter/Graph/Export API를 제공하는가.
- [ ] LangGraph 그래프(Book/Chapter/Eval)가 API에 통합되어 있는가.
- [ ] Next.js Web UI에서 프로젝트/책/챕터/실행/Export를 전부 다룰 수 있는가.
- [ ] CI/CD 파이프라인이 테스트→빌드→배포까지 자동화되어 있는가.[^1][^3]
- [ ] 비용·성능·장애를 관측할 수 있는 모니터링과 알람이 설정되어 있는가.

***

이 백서는 디렉터리 4: **Delivery Stack (Backend · Frontend · DevOps)**를 기준으로, BAAS의 “생각하는 코어”를 실제 저자가 사용할 수 있는 SaaS/내부 도구로 만들기 위한 풀스택 구조와 코드 스캐폴드를 포함합니다.[^2][^3][^1]

다음 단계로는:

- `apps/api`와 `apps/web`, `packages/workflows` 레포를 실제로 초기화하고,
- 여기 포함된 코드 블록을 그대로 옮겨 스켈레톤을 만든 뒤,
- 세부 구현(에러 처리, 인증, UI 디테일, 실제 배포 스크립트)을 채워 넣으면 됩니다.

<div align="center">⁂</div>

[^1]: https://forum.cursor.com/t/best-practices-for-structuring-a-next-js-fastapi-supabase-project/49706

[^2]: https://www.pronextjs.dev/workshops/next-js-react-server-component-rsc-architecture-jbvxk/understanding-the-example-monorepo-structure-4gpny

[^3]: https://github.com/belgattitude/nextjs-monorepo-example/blob/main/README.md

[^4]: https://github.com/cpjet64/vibecoding/blob/main/system-architecture-guide.md

[^5]: https://docs.vibe-coding-framework.com/documentation-standards

[^6]: https://cloud.google.com/discover/what-is-vibe-coding

[^7]: https://www.langchain.com/langgraph

[^8]: https://peliqan.io/blog/langchain-vs-langgraph/

[^9]: https://www.evidentlyai.com/blog/llm-applications

[^10]: https://blog.langchain.com/langgraph-multi-agent-workflows/

[^11]: https://github.com/langchain-ai/langgraph/issues/3365

