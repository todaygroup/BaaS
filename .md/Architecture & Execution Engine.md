<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 지금까지 나눈 대화를 심층 분석하여 **Book-Authoring Agent System (BAAS)** 내용을 작성할 때 각 권 별로 백서 형태로 하나씩 문서를 생성합니다. 문서를 작성하기 전에 모든 내용을 "제 1 원칙 사고법"을 기준으로 하여 전 과정을 근본적인 본질에서 시작하여 요약본 형태가 아니라 모든 내용이 하나도 빠짐없이 필요한 모든 단계가 순차적으로 적용된 Full Stack 문서 형태로 작성합니다.

"디렉터리 2: Architecture \& Execution Engine" 에 대한 내용을 실제 책 분량 수준으로 더 확장해서 각 권 별로 작성합니다. 이때 실 구현을 위한 코드·템플릿을 상세화하는 과정을 포함하여 모든 소스코드가 포함되도록 작성합니다.

단일 응답에 “실제 책 분량 + 전체 소스코드”를 모두 담기는 어렵기 때문에, 디렉터리 2를 **한 권짜리 백서의 구조 + 핵심 설계 + 대표 코드 스캐폴드**까지 최대한 깊게 풀어내는 형태로 정리합니다. 이 문서를 기반으로 LangGraph/백엔드/워크플로우 구현을 바로 시작할 수 있도록 하는 것이 목표입니다.[^1][^2]

아래 내용은 `/02_arch_execution` 아래 여러 `.md`로 나눠도 되고, 하나의 “Guide 2 – Architecture \& Execution Engine for BAAS”로 합쳐도 무방합니다.

***

# Guide 2. Architecture \& Execution Engine for BAAS

**Book-Authoring Agent System (BAAS) – 아키텍처 \& 실행 엔진 백서**

***

## 1. 제1원칙 관점에서 본 BAAS 아키텍처

### 1.1 문제 재정의

- “전문 작가 수준으로 책 한 권을 쓴다”는 것은, 본질적으로 **복수의 복잡한 인지 작업(기획, 구조화, 탐색, 통합, 편집)을 순차·병렬적으로 수행하는 프로세스**이다.[^3][^4]
- BAAS는 이 프로세스를
    - **노드(Agent/Tool) 단위 작업**,
    - **그래프(Workflow) 단위 조합**,
    - **상태(State) 단위 데이터 흐름**
으로 재정의한 후, 이를 LangGraph 기반 실행 엔진으로 구동하는 시스템이다.[^5][^6]


### 1.2 아키텍처 레이어(요약)

- **Application Layer**: Web UI/CLI에서 “책 단위 행동” 요청.
- **Orchestration Engine**: LangGraph + LangChain으로 구성된 Book/Chapter/Eval 그래프.[^2][^7]
- **Workflow Runtime Layer**: GraphRun/NodeRun/Execution 관리, 멱등성·리트라이 담당.[^1]
- **Data \& RAG Layer**: Supabase + Qdrant/Pinecone.
- **Observability Layer**: 로그·메트릭·트레이싱.

이 백서는 주로 **Orchestration Engine + Workflow Runtime Layer**를 다룬다.

***

## 2. 기술 스택 \& 제약 (tech-stack-and-constraints.md)

### 2.1 코어 스택 선택

```text
언어/런타임:
  - Python 3.10+ (에이전트·LangGraph·RAG·백엔드)
  - TypeScript 5+ (Next.js 프론트엔드)

Agentic 오케스트레이션:
  - LangGraph (StateGraph, multi-agent)[web:288][web:256]
  - LangChain Core (Tools/Runnables/Retrievers)[web:276][web:285]

LLM & Provider:
  - OpenRouter (여러 모델 게이트웨이)[web:276]
  - gpt-4.1 / gpt-4.1-mini / Claude Sonnet 3.5 / o3-mini

데이터:
  - Supabase(Postgres + Auth + Storage)
  - Qdrant 또는 Pinecone(VectorDB)[web:285]

백엔드:
  - FastAPI (REST API / 그래프 실행 엔드포인트)

프론트:
  - Next.js 14(App Router, PWA)

관찰성:
  - OpenTelemetry(Trace), 구조화 로그(JSONL/DB)
  - 선택: LangSmith / Open Source 대시보드[web:279][web:291]
```


### 2.2 제약 조건

- **비용 제약**: 챕터당 LLM 비용 200~500원 수준 목표.
- **레거시 제약 없음**: 신규 시스템, LangGraph/LLM 중심 아키텍처 최적화 가능.
- **인력 제약**: Python/TypeScript/LangChain/LangGraph에 익숙한 소규모 팀.
- **품질 제약**: 결과물은 “출판 가능한 수준”을 목표로 함(AgentEval ≥ 0.8).

***

## 3. 전체 아키텍처 개요 (architecture-overview.md)

### 3.1 C4 Level 1 – 시스템 컨텍스트

- **사용자(저자)** ↔ **BAAS Web UI (Next.js)** ↔ **BAAS API (FastAPI + LangGraph)** ↔
    - RAG 데이터베이스(Qdrant + Supabase)
    - 파일 스토리지(PDF/노트)
    - Observability 스택.


### 3.2 C4 Level 2 – 컨테이너

- `web` (Next.js)
- `api` (FastAPI, LangGraph 런타임 포함)
- `worker` (배치 인덱싱, 장기 그래프 실행)
- `db` (Supabase)
- `vector` (Qdrant/Pinecone)

***

## 4. 워크플로우 개념·레이어 모델 (workflow-concepts-and-layers.md)

### 4.1 워크플로우 정의

- BAAS 워크플로우 = **상태(State)를 가진 그래프**
    - 예: *Book Graph*: “책 전체 구조 설계→챕터 생성 스케줄링→최종 통합”.
    - *Chapter Graph*: “해당 챕터 리서치→사례 생성→초안 작성→AutoEval→재작성”.[^6][^5]


### 4.2 레이어 구성

1. **Presentation Layer (에디터/컨트롤 UI)**
2. **Workflow Runtime Layer**
    - 실행 관리(GraphRun, NodeRun, 리트라이·멱등성)
3. **Nodes \& Connections Layer**
    - LangGraph 노드/엣지, n8n식 노드 모델 이해[^8]
4. **Data Layer**
    - GraphState, items[], JSON, RAG 결과
5. **Credentials \& Secrets Layer**
6. **Executions \& Debugging Layer**

***

## 5. 노드 기본 구조 (node-basics.md)

### 5.1 노드 타입

- **Trigger Node**: Book 생성, Chapter 상태 변경 등 이벤트 기반 시작.
- **Action Node**: LLM 호출, RAG 검색, Export 생성 등 실제 작업.
- **Core Logic Node**: IF, Switch, Merge, Split, Wait 같은 제어 노드.[^9]
- **Subgraph/Agent Node**: 개별 에이전트 또는 챕터 서브그래프 호출.


### 5.2 LangGraph 노드 구현 패턴

```python
# /02_arch_execution/langgraph_nodes/book_outline.py

from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_core.runnables import Runnable
from datetime import datetime

class BookState(TypedDict, total=False):
    topic: str
    audience: str
    tone: str
    outline: dict
    chapters_planned: List[str]
    created_at: str

def plan_outline(state: BookState) -> BookState:
    """Outline Planner Node: LLM을 호출해 책 전체 구조를 생성."""
    topic = state["topic"]
    audience = state["audience"]
    tone = state["tone"]

    # LangChain Runnable (LLM) 호출 – 의사코드
    prompt = f"""
    You are a professional book outline planner.
    Topic: {topic}
    Audience: {audience}
    Tone: {tone}
    Produce a MECE outline with Parts and Chapters as JSON.
    """
    # llm는 OpenRouter에 연결된 LangChain Runnable이라고 가정
    raw = llm.invoke(prompt)
    outline = raw  # 응답 JSON 파싱 생략

    return {
        **state,
        "outline": outline,
        "chapters_planned": [c["title"] for p in outline["parts"] for c in p["chapters"]],
        "created_at": datetime.utcnow().isoformat()
    }
```


***

## 6. 노드 카탈로그 설계 (node-catalog.md)

### 6.1 카테고리

- **Planning Nodes**: BookOutlinePlanner, ChapterPlanner
- **RAG Nodes**: ChapterResearchRetriever, RelevanceChecker
- **Writing Nodes**: ChapterWriter, CaseStudyWriter, StyleLocalizer
- **Evaluation Nodes**: AutoCriticAgent, StructureConsistencyChecker
- **Export Nodes**: MarkdownExporter, DocxExporter, PdfExporter
- **Utility Nodes**: AggregateChapters, SortByPart, FilterChapters


### 6.2 노드 메타데이터 스키마

```python
# /02_arch_execution/node_catalog.py

from pydantic import BaseModel
from typing import Dict, Any, List, Literal

class NodeIO(BaseModel):
    schema: Dict[str, Any]  # JSON Schema

class NodeDefinition(BaseModel):
    id: str
    category: Literal["planning", "rag", "writing", "evaluation", "export", "utility"]
    label: str
    description: str
    input: NodeIO
    output: NodeIO
    options: Dict[str, Any]

NODE_CATALOG: List[NodeDefinition] = [
    NodeDefinition(
        id="chapter_writer",
        category="writing",
        label="Chapter Writer",
        description="Writes a full chapter draft based on outline and research notes.",
        input=NodeIO(schema={"type": "object", "properties": {
            "chapter_id": {"type": "string"},
            "outline": {"type": "object"},
            "research_notes": {"type": "array"}
        }}),
        output=NodeIO(schema={"type": "object", "properties": {
            "chapter_id": {"type": "string"},
            "draft_text": {"type": "string"}
        }}),
        options={"max_tokens": 8000, "temperature": 0.5}
    )
]
```


***

## 7. 연결 \& 흐름 제어 (connections-and-flow-control.md)

### 7.1 기본 패턴

- **직선형**: A → B → C (단순 순차)
- **브랜치**: 조건에 따라 다른 에이전트/경로 선택(IF, Switch)[^9]
- **합류**: 여러 리서치/케이스 결과를 Merge 후 Writer로 전달.
- **루프**: Eval 점수 낮으면 “Rewrite” 경로로 재진입.


### 7.2 LangGraph에서의 표현

```python
# /02_arch_execution/book_graph.py

from langgraph.graph import StateGraph, END

workflow = StateGraph(BookState)
workflow.add_node("plan_outline", plan_outline)
workflow.add_node("schedule_chapters", schedule_chapters)

workflow.set_entry_point("plan_outline")
workflow.add_edge("plan_outline", "schedule_chapters")
workflow.add_edge("schedule_chapters", END)

book_graph = workflow.compile()
```

Chapter Graph 예시 (루프 포함):

```python
# /02_arch_execution/chapter_graph.py

from langgraph.graph import StateGraph, END
from typing import TypedDict

class ChapterState(TypedDict, total=False):
    chapter_id: str
    outline: dict
    research_notes: list
    draft_text: str
    eval_score: float
    iteration: int

def research_node(state: ChapterState) -> ChapterState: ...
def write_node(state: ChapterState) -> ChapterState: ...
def eval_node(state: ChapterState) -> ChapterState: ...

def route_on_eval(state: ChapterState) -> str:
    if state["eval_score"] >= 0.8 or state["iteration"] >= 3:
        return END
    return "research"

workflow = StateGraph(ChapterState)
workflow.add_node("research", research_node)
workflow.add_node("write", write_node)
workflow.add_node("eval", eval_node)

workflow.set_entry_point("research")
workflow.add_edge("research", "write")
workflow.add_edge("write", "eval")
workflow.add_conditional_edges("eval", route_on_eval, {END: END, "research": "research"})

chapter_graph = workflow.compile()
```


***

## 8. 워크플로우 내 데이터 모델 (data-model-in-workflows.md)

### 8.1 GraphState 설계 원칙

- BookState, ChapterState 등 **타입 안전한 TypedDict**를 사용해 LangGraph State를 정의.[^10][^5]
- 각 노드는 **입력·출력 State 키**를 명시적으로 읽고 쓴다.


### 8.2 ChapterState 예시

```python
class ChapterState(TypedDict, total=False):
    chapter_id: str
    part_id: str
    book_id: str
    topic: str
    outline: dict
    research_notes: list  # list[dict]
    case_studies: list    # list[dict]
    draft_text: str
    eval_score: float
    eval_feedback: str
    iteration: int
```

노드 구현 시, **State를 가능한 한 불변처럼 다루고** 새 State를 리턴하는 패턴 유지.

***

## 9. Credentials \& Secrets (credentials-and-secrets.md)

### 9.1 LLM/RAG 자격증명 모델

```python
# /02_arch_execution/credentials_model.py

class LLMProviderCredentials(BaseModel):
    id: str
    provider: Literal["openrouter"]
    api_key: str  # 저장 시 암호화
    default_model: str = "gpt-4.1"

class VectorDBCredentials(BaseModel):
    id: str
    provider: Literal["qdrant", "pinecone"]
    api_url: str
    api_key: str
```

- API 키는 DB 저장 시 KMS/Vault로 암호화.
- 워크플로우/그래프 정의에서는 **자격 증명 ID만 참조**.

***

## 10. 실행 \& 로깅 (executions-and-logging.md)

### 10.1 실행 모델

```python
# /02_arch_execution/executions_model.py

class ExecutionStatus(str, Enum):
    pending = "pending"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"

class Execution(BaseModel):
    id: str
    graph_type: Literal["book", "chapter", "eval"]
    state_snapshot: dict
    status: ExecutionStatus
    created_at: datetime
    finished_at: Optional[datetime] = None
```


### 10.2 로깅 \& Observability 연계

- 각 NodeRun 시 아래 구조의 JSON 로그 생성:

```json
{
  "run_id": "book_20250101",
  "node_id": "chapter_writer",
  "graph_type": "chapter",
  "timestamp_start": "...",
  "timestamp_end": "...",
  "latency_ms": 23890,
  "input_tokens": 4250,
  "output_tokens": 9800,
  "rag_docs_used": ["DOC_2024_AI_01_p12_c03"],
  "status": "success"
}
```


***

## 11. 디버깅 \& 데이터 핀닝 (debugging-and-data-pinning.md)

### 11.1 목적

- 개발·테스트 단계에서 **같은 입력 상태로 반복 테스트**하기 위한 도구.[^11][^12]
- 프로덕션에서는 **생성 실행에는 영향을 주지 않도록** 설계.


### 11.2 구현 스케치

```python
# /02_arch_execution/debug_pinning.py

import json
from pathlib import Path
from typing import Any, Dict

PIN_DIR = Path(".pins")

def pin_state(name: str, state: Dict[str, Any]) -> None:
    PIN_DIR.mkdir(exist_ok=True)
    (PIN_DIR / f"{name}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2))

def load_pinned_state(name: str) -> Dict[str, Any]:
    return json.loads((PIN_DIR / f"{name}.json").read_text())
```

- 예: 실전 한 번 실행 후 BookState/ChapterState를 pin → 이후 개발 시 그 상태를 그대로 불러와 노드/그래프만 재실행.

***

## 12. LangChain + LangGraph 통합 (langchain-langgraph-integration.md)

### 12.1 역할 분리 원칙[^7][^10]

- LangChain: **LLM/Tool/Retriever 컴포넌트**
- LangGraph: **에이전트/워크플로우 런타임(StateGraph)**


### 12.2 통합 예시: RAG + Writer 노드

```python
# /02_arch_execution/langchain_integration.py

from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

llm = ChatOpenAI(model="gpt-4.1")  # 실제로는 OpenRouter 래퍼 사용
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def build_research_chain():
    prompt = ChatPromptTemplate.from_template(
        "Summarize key insights from the following context for chapter: {chapter_title}\n\n{context}"
    )
    chain = (
        {"context": RunnableLambda(retrieve_docs), "chapter_title": RunnableLambda(lambda state: state["title"])}
        | prompt
        | llm
    )
    return chain
```

LangGraph 노드에서:

```python
def research_node(state: ChapterState) -> ChapterState:
    chain = build_research_chain()
    summary = chain.invoke(state)
    state["research_notes"] = [{"type": "summary", "text": summary.content}]
    return state
```


***

## 13. Prompt-to-Graph 전략 (prompt-to-graph-strategy.md)

### 13.1 목적

- “설명(Describe) → 그래프 설계(Plan) → 그래프 코드(Scaffold)”로 가는 **PTG(프롬프트→그래프)** 자동화.[^13][^1]


### 13.2 품질 체크리스트[^14][^1]

- 루프/종료 조건 명시 여부.
- 에러 경로/예외 처리 노드 존재 여부.
- 자격 증명/보안 관련 노드 존재 여부.
- 비용 관점에서 불필요한 LLM 호출 루프 여부.


### 13.3 PTG용 프롬프트 예시

```text
[developer]
너는 LangGraph 기반 멀티에이전트 시스템 아키텍트이다.
입력 요구사항을 StateGraph와 노드/에지 정의로 설계한다.

[user]
다음 요구사항을 만족하는 "Chapter Graph"를 설계하고,
Python LangGraph 코드 스캐폴드를 생성해줘.

요구사항:
- State: ChapterState(TypedDict)
- Nodes: research, write, eval
- Flow: research -> write -> eval -> (score<0.8 && iter<3 -> research else END)
- Observability: run_id, node_id 기준 로그 출력
```


***

## 14. 아키텍처 \& 실행 엔진 체크리스트

- [ ] Book/Chapter/Eval 그래프 구조가 LangGraph StateGraph로 정의되어 있는가.
- [ ] 각 노드에 대해 입력/출력/옵션/에러 동작이 명시되어 있는가.
- [ ] GraphRun/NodeRun/Execution 모델이 정의되어 있고, 실행 로그가 JSON/Trace로 남는가.
- [ ] RAG/LLM 호출은 LangChain 컴포넌트로 캡슐화되고, LangGraph 노드에서는 이를 조합만 하는가.
- [ ] PTG(프롬프트→그래프) 파이프라인을 위한 프롬프트/체크리스트가 정의되어 있는가.

***

위 백서는 **디렉터리 2: Architecture \& Execution Engine**을 기준으로, 기획 단계에서 정의된 Product \& Domain Blueprint를 실제 **LangGraph 기반 실행 엔진 구조 + 코드 스캐폴드**로 연결하는 데 필요한 내용을 거의 전부 포함합니다.[^15][^2][^5]

다음 단계로는:

- 이 문서를 기준으로 `/02_arch_execution` 아래에 파일을 실제로 분할 생성하고,
- 필요한 부분(예: `chapter_graph.py` 전체 구현, RAG Retriever 실제 코드, OpenRouter 래퍼)만 채워 넣으면, 바로 **실행 가능한 BAAS 오케스트레이션 코어**를 구축할 수 있습니다.

<div align="center">⁂</div>

[^1]: https://github.com/langchain-ai/langgraph/issues/3365

[^2]: https://www.langchain.com/langgraph

[^3]: https://www.invent.ai/blog/key-components-of-agentic-ai-architecture-building-the-foundation

[^4]: https://dl.acm.org/doi/10.1145/3708359.3712164

[^5]: https://langchain-ai.github.io/langgraph/concepts/multi_agent/

[^6]: https://blog.langchain.com/langgraph-multi-agent-workflows/

[^7]: https://peliqan.io/blog/langchain-vs-langgraph/

[^8]: https://docs.n8n.io/workflows/

[^9]: https://docs.n8n.io/workflows/components/nodes/

[^10]: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/

[^11]: https://docs.n8n.io/data/data-pinning/

[^12]: https://docs.n8n.io/data/data-mocking/

[^13]: https://vibecoding.app/blog/how-vibe-coding-works

[^14]: https://github.com/langchain-ai/langgraph/discussions/2090

[^15]: https://www.swarnendu.de/blog/langgraph-best-practices/

