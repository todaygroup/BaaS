<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 지금부터  ***Book-Authoring Agent System (BAAS)**을 위한 AI Agetn 설계 및 개발 그리고 AI Agent 서비스 구축 및 운영하기 위한 절차에 대한 Full stack Guide Line을 각 단계별로 하나하나의 별도의 가이드 북 형태로 문서화 작업을 진행해 주세요.

**Book-Authoring Agent System (BAAS)**

”한 사람의 전문 작가처럼, 한 권의 책을 기획 → 집필 → 구조 완성 → 챕터 통합 → 에디팅 → 최종 원고 생성”까지 자동화하는 Book-Writing Pipeline 구축

디렉터리 1: Product \& Domain Blueprint
디렉터리 2: Architecture \& Execution Engine
디렉터리 3: LLM · RAG · Agentic Layer
디렉터리 4: Delivery Stack (Backend · Frontend · DevOps)
디렉터리 5: UX · Interaction · Ops Runbook

지금까지 나눈 대화를 심층 분석하여 **Book-Authoring Agent System (BAAS)** 내용을 작성할 때 각 권 별로 백서 형태로 하나씩 문서를 생성합니다. 문서를 작성하기 전에 모든 내용을 "제 1 원칙 사고법"을 기준으로 하여 전 과정을 근본적인 본질에서 시작하여 요약본 형태가 아니라 모든 내용이 하나도 빠짐없이 필요한 모든 단계가 순차적으로 적용된 Full Stack 문서 형태로 작성합니다.

아래 "디렉터리 1: Product \& Domain Blueprint" 에 대한 내용을 실제 책 분량 수준으로 더 확장해서 각 권 별로 작성합니다. 이때 실 구현을 위한 코드·템플릿을 상세화하는 과정을 포함하여 모든 소스코드가 포함되도록 작성합니다.

요청하신 방식(“실제 책 분량 + 모든 소스코드까지 포함하는 풀스택 백서”)은 단일 답변에 담기에는 분량 제약을 훨씬 초과합니다. 그래서 디렉터리 1을 기준으로, **한 권짜리 백서의 구조와 핵심 본문/예시/코드 스캐폴드를 최대한 깊게 까는 1차 버전**을 제시하겠습니다. 이후 챕터별로 추가 확장을 계속 이어가면 실제 책 분량에 도달할 수 있습니다.[^1]

아래 내용은 그대로 `/01_product_domain` 아래 여러 `.md`로 쪼개도 되고, 하나의 “Guide 1 – Product \& Domain Blueprint for BAAS” 단일 문서로 합쳐도 됩니다.

***

# Guide 1. Product \& Domain Blueprint for BAAS

**Book-Authoring Agent System (BAAS) – Product \& Domain Blueprint**

***

## 1. 서론

### 1.1 문서의 목적

- 이 문서는 **Book-Authoring Agent System (BAAS)**를 “기획–설계–구현–운영” 전체 수명주기 기준으로 바라볼 때, 그 중 **제품 기획·도메인 모델링 레이어**를 정교하게 정의하기 위한 백서이다.[^2][^3]
- 후속 아키텍처/LLM/RAG/오케스트레이션/UX/운영 가이드들이 모두 이 문서의 정의를 **단일 소스 오브 트루스(Single Source of Truth)**로 참조하도록 설계한다.[^4]


### 1.2 제1원칙(First Principles) 관점

- “책 한 권을 쓴다”는 행위는, **정보의 수집·구조화·변환·표현**이라는 연속된 프로세스이다.[^3]
- BAAS는 이 프로세스를 **에이전트·그래프·RAG·LLM** 관점에서 재해석한 시스템이며, 사람(저자)은 *방향성·판단·최종 승인*에 집중하고 나머지는 시스템에 위임하는 것을 목표로 한다.[^5][^6]

***

## 2. BAAS 비전·목표·성공지표

### 2.1 비전 선언문(Vision Statement)

> “BAAS는 한 사람의 저자가 수년간 쌓아온 지식과 스타일을 AI 에이전트 팀에 이식하여, **책 한 권 전체를 고품질로 자동 집필**할 수 있게 만드는 지적 생산 인프라이다.”[^7][^2]

핵심 키워드:

- **Author-Centric**: 저자의 고유 관점/스타일이 중심.
- **Agentic**: 다중 에이전트 팀이 협업해 완성.
- **Reusable Knowledge**: 한 번 구축한 지식·워크플로우로 여러 책/콘텐츠 생산.


### 2.2 목적(Goals)

- **G1. 시간 단축**: 책 한 권 집필 시간을 기존 대비 80% 이상 단축.
- **G2. 품질 유지/개선**: Auto Critic + Human Review를 통해 기존 저서 대비 동등 이상 품질 유지.
- **G3. 확장성**: 동일 시스템으로 저자 1명 → 저자 여러 명, 단행본 → 시리즈/교재/워크북까지 확장 가능.


### 2.3 North Star Metric \& KPI

- **NSM**:
    - “BAAS를 사용해 **완성된 원고(80% 이상 Human 편집 완료 상태)**로 통합된 책 권수 / 저자 수”
- **핵심 KPI 예**:
    - K1: 챕터당 평균 생성 시간
    - K2: 챕터당 평균 수정 비율(인간 수정 토큰 수 / 총 토큰 수)
    - K3: AgentEval 평균 점수 (0~1 스케일)
    - K4: 한 번 설정한 RAG 인덱스를 활용해서 생성된 추가 책/리포트 수[^2]

```yaml
# /01_product_domain/vision-and-goals.example.yml
vision: >
  AI agents that can plan, research, draft, and refine an entire
  book as a single professional author would, using the author's
  own knowledge and style.

north_star_metric:
  name: "books_completed_per_author"
  definition: "Count of books that reach 80%+ human-reviewed quality using BAAS."
kpis:
  - id: "chapter_time_minutes"
    target: "<= 2"
  - id: "chapter_revision_ratio"
    target: "<= 0.2"
  - id: "agenteval_score"
    target: ">= 0.8"
  - id: "books_per_rag_index"
    target: ">= 3"
```


***

## 3. 타깃 사용자·페르소나·세그먼트

### 3.1 1차 페르소나: “해님” (전략 컨설턴트·저자)

- 역할: 전략 컨설턴트, 강연자, 저자.
- Pain:
    - 대량의 노트·리포트·슬라이드가 **책 구조로 재조합되지 못하고 묻혀 있음**.
    - 집필 시간/에너지 부족, 장기 프로젝트 유지 어려움.
- 목표:
    - 본인의 전략·프레임워크를 “책/강의/워크북” 등 다양한 포맷으로 빠르게 확장.[^7]


### 3.2 2차 페르소나

- 전문 강사·인플루언서: 강의 콘텐츠 → 책·전자책.
- 기업 내부 컨설턴트: 정기 리포트·백서 → 책 형식의 Thought Leadership 자료.
- 출판사/콘텐츠팀: 여러 저자와 협업하는 편집/기획 담당자.


### 3.3 세그먼트 구분

- 규모: 1인 저자, 스몰 팀(2~5명), 조직(10명 이상)
- 도메인: 전략/마케팅/기술/교육 등
- 언어: 한국어 중심 → 영어/다국어 확장
- 플랜: **개인(Author)** / **팀(Studio)** / **엔터프라이즈(Publisher)**

```yaml
# /01_product_domain/personas-and-segments.example.yml
personas:
  - id: "author-hanim"
    role: "Strategic consultant & author"
    pains:
      - "Too many scattered notes and reports."
      - "Not enough time to structure and write a full book."
    goals:
      - "Turn consulting IP into 1–2 books per year."
segments:
  - id: "solo-author"
    description: "Single author with own IP library"
  - id: "team-studio"
    description: "Small content studio / consulting team"
  - id: "enterprise-publisher"
    description: "Publishing / L&D org building multiple titles"
```


***

## 4. 도메인 모델링 (엔티티·관계·이벤트)

### 4.1 핵심 엔티티 정의

**핵심 질문**: “책 한 권을 자동 집필하는 시스템에서, *어떤 객체*들이 반드시 존재해야 하는가?”

- Author
- Workspace / Project
- Book
- Part / Chapter / Section (구조)
- AgentRun / GraphRun / NodeRun (에이전트 실행)
- KnowledgeSource / Document / Chunk / Vector
- EvalResult (AgentEval)
- ExportArtifact (MD/DOCX/PDF/JSON)


#### 4.1.1 Author / Workspace / Project

```python
# /01_product_domain/domain_model.py

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Author(BaseModel):
    id: str
    name: str
    email: str
    locale: str = "ko-KR"
    time_zone: str = "Asia/Seoul"

class Workspace(BaseModel):
    id: str
    name: str
    owner_id: str
    members: List[str]
    created_at: datetime

class Project(BaseModel):
    id: str
    workspace_id: str
    name: str
    description: Optional[str] = None
    status: Literal["draft", "active", "archived"] = "draft"
    created_at: datetime
```


#### 4.1.2 Book / Part / Chapter 구조

```python
class Book(BaseModel):
    id: str
    project_id: str
    title: str
    subtitle: Optional[str] = None
    target_audience: str
    tone: str  # e.g. "strategic, friendly, Korean"
    language: str = "ko"
    status: Literal["outline", "drafting", "editing", "completed"] = "outline"
    created_at: datetime

class Part(BaseModel):
    id: str
    book_id: str
    order: int
    title: str
    description: Optional[str] = None

class Chapter(BaseModel):
    id: str
    book_id: str
    part_id: Optional[str]
    order: int
    title: str
    purpose: str  # what this chapter must achieve
    status: Literal["planned", "researching", "drafted", "revising", "final"] = "planned"
```


### 4.2 에이전트 실행·평가 도메인

```python
class GraphRun(BaseModel):
    id: str
    project_id: str
    book_id: Optional[str]
    graph_type: Literal["book", "chapter", "eval"]
    status: Literal["pending", "running", "succeeded", "failed"]
    started_at: datetime
    finished_at: Optional[datetime] = None

class NodeRun(BaseModel):
    id: str
    graph_run_id: str
    node_id: str
    agent_role: str  # e.g. "chapter_writer"
    status: Literal["pending", "running", "succeeded", "failed"]
    input_tokens: int
    output_tokens: int
    latency_ms: int
    rag_docs_used: List[str]
    error_message: Optional[str] = None

class EvalResult(BaseModel):
    id: str
    node_run_id: str
    score_overall: float
    score_structure: float
    score_logic: float
    score_style: float
    comments: str
```


***

## 5. 정보 아키텍처 \& URL 구조

### 5.1 상위 정보 계층

- Workspace → Project → Book → Part/Chapter → GraphRun/Execution → Export
- 사용자 UI는 아래 네 비주얼 영역을 핵심으로 한다.
    - **Dashboard**: 여러 프로젝트/책/상태 요약
    - **Book Overview**: 책 구조(Part/Chapter) 트리
    - **Chapter Workspace**: 특정 챕터의 리서치/작성/평가 상태
    - **Exports**: 최종 원고들(MD/DOCX/PDF/JSON)


### 5.2 URL 패턴 (Next.js 기준)

```text
/workspaces/:workspaceId/projects/:projectId/books/:bookId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/chapters/:chapterId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/graphs/:graphRunId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/exports
```

```ts
// /01_product_domain/information-architecture.example.ts

export const routes = {
  bookOverview: (wsId: string, projId: string, bookId: string) =>
    `/workspaces/${wsId}/projects/${projId}/books/${bookId}`,
  chapterWorkspace:
    (wsId: string, projId: string, bookId: string, chapterId: string) =>
      `/workspaces/${wsId}/projects/${projId}/books/${bookId}/chapters/${chapterId}`,
};
```


***

## 6. 요구사항 (기능/비기능) – BAAS 전용

### 6.1 기능 요구사항 (요약 → 시스템 객체로 매핑)

#### 6.1.1 새 책 기획

- 입력: 주제, 독자, 톤, 분량, 목표(예: “AI 전략 실무자용, 250p”)
- 처리: Outline Planner가 MECE 기반 Part/Chapter 구조 생성 → Book/Part/Chapter 레코드 생성 → BookState 저장.
- 출력: Book/Part/Chapter JSON + UI 트리.

```json
// /01_product_domain/requirements-functional-nonfunctional.example.book-outline.json
{
  "input": {
    "topic": "Agentic AI for Business Strategy",
    "audience": "Korean strategy leaders and consultants",
    "tone": "전략적이지만 친근한 한국어",
    "target_length": "12 chapters"
  },
  "output": {
    "book": { "id": "book_001", "title": "에이전틱 AI 전략 실무" },
    "parts": [...],
    "chapters": [...]
  }
}
```


#### 6.1.2 챕터 작성 플로우

- 상태 전이: `planned → researching → drafted → revising → final`
- 각 상태는 최소한 다음 *에이전트/그래프 실행*과 매핑된다:
    - researching: Research Agent + RAG
    - drafted: Chapter Writer
    - revising: Auto Critic + 재작성
    - final: Human 승인.


### 6.2 비기능 요구사항

- 성능: 챕터 생성 40초~2분, Outline 생성 10~30초.
- 품질: AgentEval ≥ 0.75, Auto Critic 실패 시 자동 재시도 ≤ N회.
- 재현성: `temperature` 낮은 값, seed 고정 옵션 제공.
- 보안: 저자별 RAG 인덱스 분리(워크스페이스 단위 멀티테넌시).[^8]

***

## 7. 도메인 이벤트 \& 워크플로우 트리거

### 7.1 이벤트 카탈로그

```yaml
# /01_product_domain/domain-events-and-triggers.example.yml
events:
  - id: "BookCreated"
    payload: ["book_id", "project_id", "author_id"]
  - id: "ChapterStatusChanged"
    payload: ["chapter_id", "old_status", "new_status"]
  - id: "GraphRunCompleted"
    payload: ["graph_run_id", "status", "graph_type"]
  - id: "EvalResultRecorded"
    payload: ["eval_result_id", "node_run_id", "score_overall"]
triggers:
  - on: "BookCreated"
    start_graph: "book_outline_eval_graph"
  - on: "ChapterStatusChanged"
    when:
      new_status: "researching"
    start_graph: "chapter_research_graph"
```


***

## 8. Product Planning \& Slice 전략

### 8.1 수직 슬라이스(Vertical Slice)

- Slice 1: “단일 챕터 BAAS” (한 챕터만 완전 자동 생성)
- Slice 2: “책 전체 아웃라인 + 챕터 1~3까지 자동 생성”
- Slice 3: “전체 책 + AutoEval + Export”

각 Slice는 다음 공통 구조를 가진다:

- Product 문서(PRD)
- Domain 모델 확장
- Graph 정의(LangGraph)
- RAG 세팅
- UI 최소 플로우.

```yaml
# /01_product_domain/development-plan.example.yml
milestones:
  - id: "slice1_single_chapter"
    scope:
      - "Single Book"
      - "Single Chapter BAAS flow"
    includes:
      - "ChapterState schema"
      - "chapter_graph v0.1"
      - "basic RAG integration"
```


***

## 9. Product 체크리스트

- [ ] 비전·미션·NSM이 한 문서에서 명확히 정의되었는가.
- [ ] 핵심 페르소나(해님 포함)를 기준으로 한 주요 Use Case가 도출되었는가.
- [ ] Book/Part/Chapter/GraphRun/Eval/Export 등 핵심 도메인 엔티티와 관계가 정의되었는가.
- [ ] URL/IA 구조가 Workspace → Project → Book → Chapter → GraphRun으로 일관성 있게 설계되었는가.
- [ ] Slice 1~3까지의 제품·기술 범위가 명확히 나뉘어 있는가.
- [ ] 이 문서 내용만으로도 LangGraph/LLM/RAG/프론트엔드 팀이 구현을 시작할 수 있는가.

***

여기까지가 **디렉터리 1: Product \& Domain Blueprint**를 한 권짜리 백서 기준으로 “근본 구조 + 핵심 예시 + 도메인 모델 코드 + 설정 예시”까지 포함한 1차 버전입니다.[^6][^3][^2]

다음 턴에서는, 원하시는 방향에 따라:

- `domain-modeling.md`만 따로 더 깊게(예: 스타일 학습용 AuthorStyleProfile 엔티티, KnowledgeSource 온톨로지, ExportArtifact 세부 구조)를 확장하거나,
- 혹은 Guide 2 (Architecture \& Execution Engine)로 넘어가 LangGraph/Workflow 레벨의 설계를 같은 방식으로 풀어낼 수 있습니다.

<div align="center">⁂</div>

[^1]: https://docs.vibe-coding-framework.com/documentation-standards

[^2]: https://www.codersarts.com/post/a-complete-guide-to-creating-a-multi-agent-book-writing-system-part-3

[^3]: https://dl.acm.org/doi/10.1145/3708359.3712164

[^4]: https://hbr.org/2025/10/designing-a-successful-agentic-ai-system

[^5]: https://illuminaire.io/agentic-ai-as-collaborator-is-rewriting-the-creative-operating-system/

[^6]: https://www.evidentlyai.com/blog/llm-applications

[^7]: https://coda.io/@helen-king/ai-powered-publishing-use-cases

[^8]: https://www.arionresearch.com/blog/the-architecture-of-agentic-ai-building-systems-that-think-and-act-autonomously

