<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 지금까지 나눈 대화를 심층 분석하여 **Book-Authoring Agent System (BAAS)** 내용을 작성할 때 각 권 별로 백서 형태로 하나씩 문서를 생성합니다. 문서를 작성하기 전에 모든 내용을 "제 1 원칙 사고법"을 기준으로 하여 전 과정을 근본적인 본질에서 시작하여 요약본 형태가 아니라 모든 내용이 하나도 빠짐없이 필요한 모든 단계가 순차적으로 적용된 Full Stack 문서 형태로 작성합니다.

"디렉터리 3: LLM · RAG · Agentic Layer " 에 대한 내용을 실제 책 분량 수준으로 더 확장해서 각 권 별로 작성합니다. 이때 실 구현을 위한 코드·템플릿을 상세화하는 과정을 포함하여 모든 소스코드가 포함되도록 작성합니다.

단일 응답에 “책 분량 + 전체 소스코드”를 모두 담을 수는 없으므로, 디렉터리 3을 **한 권짜리 백서 구조 + 핵심 설계 + 대표 코드/템플릿 스캐폴드**까지 최대한 깊게 펼친 1차 버전으로 작성합니다. 이 문서를 기반으로 실제 레포에서 파일만 쪼개면 바로 BAAS의 LLM·RAG·Agent 레이어를 구현할 수 있습니다.[^1][^2][^3][^4]

아래는 “Guide 3 – LLM · RAG · Agentic Layer for BAAS”로 보는 단일 백서 구조입니다.

***

# Guide 3. LLM · RAG · Agentic Layer for BAAS

**Book-Authoring Agent System (BAAS) – LLM·RAG·에이전트 레이어 백서**

***

## 1. 제1원칙: BAAS에 필요한 “생각하는 레이어” 정의

### 1.1 본질적 질문

- “책 한 권을 AI가 쓰게 하려면, AI에게 어떤 **인지 능력**과 **정보 구조**를 줘야 하는가?”
- 최소 요구 능력:[^5][^6]
    - 주제·독자·톤을 이해하고 → 책 구조로 계획(Planning)
    - 필요한 정보를 찾아서(Research/RAG) → 정리·요약(Synthesis)
    - 전체 구조와 스타일을 유지하며 장문을 생성(Writing)
    - 자기 평가·비판·수정(Evaluation/Refinement)


### 1.2 LLM·RAG·Agentic의 역할 분리

- **LLM Layer**:
    - “생성/추론” 엔진. 모델 선택·토큰·비용·출력 안정성을 관리.
- **RAG Layer**:
    - 저자의 지식/외부 자료를 LLM이 사용할 수 있는 형태로 제공.
- **Agentic Layer(LangGraph)**:
    - 플래너·리서처·라이터·크리틱 등 역할을 가진 에이전트 팀이, 상태를 공유하며 협업하는 그래프.[^3][^7]

이 가이드는 이 세 레이어가 **BAAS에서 어떻게 상호작용하는지**를 모두 정의한다.

***

## 2. LLM Provider \& OpenRouter 전략 (llm-provider-strategy-openrouter.md)

### 2.1 왜 OpenRouter 기반인가

- 여러 모델을 상황별로 선택해 **비용·성능 최적화**.[^1]
- 공급자 락인 최소화, 지역 규제/모델 별 제약 회피.
- BAAS는 역할별로 **모델을 다르게 쓰는 설계**가 핵심이므로, 라우팅 유연성이 중요.


### 2.2 역할별 모델 매핑 규칙

PRD에서 정의한 역할–모델 매핑을 LLM 라우터 규칙으로 형식화:

```python
# /03_llm_rag_agents/llm_router.py

from typing import Literal, Dict, Any

AgentRole = Literal[
    "book_supervisor",
    "outline_planner",
    "research_agent",
    "case_study_agent",
    "chapter_writer",
    "structure_consistency_agent",
    "style_localization_agent",
    "auto_critic",
    "marketing_agent",
]

ROLE_MODEL_MAP: Dict[AgentRole, Dict[str, Any]] = {
    "book_supervisor": {"model": "gpt-4.1-mini", "temperature": 0.3},
    "outline_planner": {"model": "gpt-4.1", "temperature": 0.4},
    "research_agent": {"model": "gpt-4.1", "temperature": 0.2},
    "case_study_agent": {"model": "gpt-4.1", "temperature": 0.7},
    "chapter_writer": {"model": "gpt-4.1", "temperature": 0.5},
    "structure_consistency_agent": {"model": "gpt-4.1-mini", "temperature": 0.2},
    "style_localization_agent": {"model": "gpt-4.1", "temperature": 0.4},
    "auto_critic": {"model": "gpt-4.1-mini", "temperature": 0.1},
    "marketing_agent": {"model": "gpt-4.1", "temperature": 0.7},
}
```

환경별 기본/대체 모델:

```python
ENV_MODEL_DEFAULTS = {
    "dev": {
        "default": "gpt-4.1-mini",
        "fallback": "o3-mini",
    },
    "prod": {
        "default": "gpt-4.1",
        "fallback": "gpt-4.1-mini",
    },
}
```


### 2.3 OpenRouter 래퍼(공통 클라이언트)

```python
# /03_llm_rag_agents/openrouter_client.py

import os
from typing import Dict, Any
import httpx

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

class OpenRouterClient:
    def __init__(self, agent_role: str, env: str = "prod"):
        from .llm_router import ROLE_MODEL_MAP, ENV_MODEL_DEFAULTS
        self.agent_role = agent_role
        self.env = env
        self.model_config = ROLE_MODEL_MAP[agent_role]
        self.default_model = ENV_MODEL_DEFAULTS[env]["default"]

    async def chat(self, messages: list[dict], **overrides: Any) -> Dict[str, Any]:
        payload = {
            "model": overrides.get("model") or self.model_config["model"] or self.default_model,
            "messages": messages,
            "temperature": overrides.get("temperature", self.model_config.get("temperature", 0.3)),
        }
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(f"{OPENROUTER_BASE_URL}/chat/completions",
                                     json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()
```


***

## 3. LLM Layer Architecture (llm-layer-architecture.md)

### 3.1 공통 호출 레이어 설계

- 책임:[^2]
    - Role → 모델/파라미터 매핑
    - 호출 로깅(run_id, node_id, tokens, latency)
    - 실패·재시도·백오프
    - 출력 형식(JSON 구조화/파싱)

```python
# /03_llm_rag_agents/llm_layer.py

from typing import Any, Dict, List
from time import perf_counter
from .openrouter_client import OpenRouterClient
from ..observability.logger import log_llm_call  # /04_delivery_stack에서 실제 구현

async def llm_call(
    agent_role: str,
    messages: List[Dict[str, str]],
    run_id: str,
    node_id: str,
    **overrides: Any,
) -> Dict[str, Any]:
    client = OpenRouterClient(agent_role)
    t0 = perf_counter()
    try:
        resp = await client.chat(messages, **overrides)
        t1 = perf_counter()
        usage = resp.get("usage", {})
        log_llm_call(
            run_id=run_id,
            node_id=node_id,
            model=resp.get("model", ""),
            latency_ms=int((t1 - t0) * 1000),
            input_tokens=usage.get("prompt_tokens", 0),
            output_tokens=usage.get("completion_tokens", 0),
            status="success",
        )
        return resp
    except Exception as e:
        t1 = perf_counter()
        log_llm_call(
            run_id=run_id,
            node_id=node_id,
            model="unknown",
            latency_ms=int((t1 - t0) * 1000),
            input_tokens=0,
            output_tokens=0,
            status="error",
            error=str(e),
        )
        raise
```


***

## 4. 프롬프트 아키텍처 \& Role 체계 (prompt-roles-and-instruction-hierarchy.md)

### 4.1 5가지 역할의 원칙[^8][^9][^10]

- **developer**: BAAS 전역 행동 규칙·보안·톤·출력 형식 등 “헌법” 수준 규칙.
- **system**: 현재 책/챕터 상태·컨텍스트·RAG 요약·실행 맥락.
- **user**: 저자/운영자가 내리는 지시(“이 챕터를 이렇게 써줘”).
- **assistant**: 모델의 응답(초안·리뷰·코드 등).
- **tool**: RAG/툴 호출 결과를 구조화된 JSON으로 전달.[^11]


### 4.2 developer 프롬프트 예시

```python
DEVELOPER_PROMPT = """
You are an AI agent working inside the Book-Authoring Agent System (BAAS).
You ALWAYS follow these rules:
1) Preserve the author's perspective, domain expertise, and tone.
2) Prefer structured outputs (JSON, Markdown with headings) whenever possible.
3) Never fabricate hard facts when RAG says context is insufficient; explicitly say so.
4) For Korean content, write in clear, professional Korean suitable for a published business book.
"""
```


### 4.3 system 컨텍스트 템플릿

```python
def build_system_context(book_meta: dict, chapter_meta: dict, rag_summary: str | None) -> str:
    return f"""
[BOOK METADATA]
Title: {book_meta['title']}
Audience: {book_meta['audience']}
Tone: {book_meta['tone']}

[CHAPTER METADATA]
Title: {chapter_meta['title']}
Purpose: {chapter_meta['purpose']}
Order: {chapter_meta['order']}

[RAG SUMMARY]
{rag_summary or '(No RAG context available or relevant.)'}
"""
```


***

## 5. Prompt Templates \& Patterns (prompt-templates-and-patterns.md)

### 5.1 챕터 작성 프롬프트 패턴

```python
def build_chapter_writer_messages(
    book_meta: dict,
    chapter_meta: dict,
    outline: dict,
    research_notes: list[dict],
    rag_citations: list[str],
) -> list[dict]:
    system_msg = {
        "role": "system",
        "content": build_system_context(book_meta, chapter_meta, rag_summary="\n\n".join(
            n["text"] for n in research_notes
        )),
    }
    user_msg = {
        "role": "user",
        "content": f"""
아래 정보를 바탕으로 이 챕터의 초안을 작성해줘.

[요구사항]
- 제목과 소제목을 명확히 구조화할 것
- 사례와 인사이트를 적절히 섞되, 과장하지 말 것
- 마케팅 문구가 아니라, 전략 컨설팅 리포트 스타일에 가깝게

[출력 형식]
- Markdown
- H2: 챕터 제목 (이미 정해져 있으면 재사용)
- H3: 주요 섹션 제목
- 필요한 경우 Bullet/Numbered list 사용

[Outline JSON]
{outline}

[RAG 문맥 출처 ID]
{rag_citations}
""",
    }
    return [
        {"role": "system", "content": DEVELOPER_PROMPT},
        system_msg,
        user_msg,
    ]
```

이 패턴을 Planner/Research/CaseStudy/AutoCritic 등에 각각 정의한다.

***

## 6. Prompt Library 구조 (prompt-library-structure.md)

```text
/03_llm_rag_agents/prompts/
  developer/
    global_rules.md
    safety_policies.md
  system/
    book_context.md
    chapter_context.md
  user/
    plan_book.md
    write_chapter.md
    evaluate_chapter.md
  tool/
    rag_result_format.md
    eval_result_format.md
```

각 파일에는 “프롬프트 텍스트 + 사용 예시 + 버전 메타데이터”를 포함.

```yaml
# /03_llm_rag_agents/prompts/metadata.yml
prompts:
  - id: "write_chapter_v1"
    path: "user/write_chapter.md"
    purpose: "Full chapter draft for strategic business books"
    version: "1.0.0"
    created_at: "2025-01-01"
```


***

## 7. 멀티에이전트 아키텍처 (multi-agent-architecture.md)

### 7.1 BAAS 에이전트 팀 구조[^12][^3]

- **Book Supervisor**: 전체 플로우 관리, 실패 시 재계획.
- **Outline Planner**: BookState 기반 Part/Chapter 구조 설계.
- **Research Agent**: Part/Chapter별 RAG 검색 + 요약.
- **Case Study Agent**: 사례 생성(실제/가상) 및 구조화.
- **Chapter Writer**: 장문 초안 생성.
- **Structure Consistency Agent**: 구조 통일·중복 검출.
- **Style Localization Agent**: 문체·톤 통일.
- **Auto Critic**: 품질 평가·점수·개선안 제시.
- **Marketing Agent**: 제목·카피·블럽 생성.


### 7.2 GraphState 설계 (예: BookState, ChapterState)

```python
# /03_llm_rag_agents/states.py

from typing import TypedDict, List, Optional

class BookState(TypedDict, total=False):
    book_id: str
    topic: str
    audience: str
    tone: str
    outline: dict
    parts: List[dict]
    chapters: List[dict]
    errors: List[str]

class ChapterState(TypedDict, total=False):
    chapter_id: str
    book_id: str
    part_id: Optional[str]
    title: str
    purpose: str
    outline: dict
    research_notes: List[dict]
    case_studies: List[dict]
    draft_text: str
    eval_score: float
    eval_feedback: str
    iteration: int
    errors: List[str]
```


***

## 8. Agent Patterns \& Best Practices (agent-patterns-and-best-practices.md)

### 8.1 Supervisor/Worker 패턴[^13][^12]

- Supervisor:
    - Book 전체 상태 관점에서 “어떤 챕터를 언제 생성/재생성할지” 결정.
- Worker:
    - Chapter Graph를 실행해 한 챕터에 집중.


### 8.2 Reflection 패턴

- Chapter Writer → Auto Critic → (점수 < threshold) → 재작성 루프.
- GraphRecursionError 방지를 위해 iteration/step 수 제한.[^12]

```python
def eval_node(state: ChapterState) -> ChapterState:
    # ... Auto Critic 호출, eval_score 업데이트
    if state["eval_score"] < 0.8:
        state["iteration"] = state.get("iteration", 0) + 1
    return state

def route_on_eval(state: ChapterState) -> str:
    if state["eval_score"] >= 0.8:
        return "finalize"
    if state.get("iteration", 0) >= 3:
        state.setdefault("errors", []).append("Max iterations reached")
        return "finalize"
    return "research"
```


***

## 9. 데이터 \& RAG 인프라 (data-rag-infra.md)

### 9.1 벡터 스키마 설계[^14][^2]

```python
# /03_llm_rag_agents/rag/schema.py

from pydantic import BaseModel
from typing import List, Literal, Dict, Any

Level = Literal["concept", "framework", "case", "data"]

class ChunkMetadata(BaseModel):
    source: str           # filename or URL
    page: int
    section: str
    topics: List[str]
    level: Level
    part_candidates: List[int]
    language: str = "ko"
    created_at: str
```


### 9.2 Qdrant/Pinecone 컬렉션 설계

- 컬렉션: `baas_author_{workspace_id}`
- 벡터: 임베딩(text-embedding-3-large)
- 페이로드: `ChunkMetadata.dict()`.


### 9.3 Chunking \& 인덱싱 파이프라인

```python
# /03_llm_rag_agents/rag/ingest_pdf.py

import pdfplumber
from datetime import datetime
from .schema import ChunkMetadata
from .vector_store import VectorStore

def ingest_pdf(path: str, part_candidates: list[int], topics: list[str]) -> None:
    chunks = []
    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            # 간단히 문단 단위 → 토큰 기준 chunking은 실제 구현에서 추가
            for paragraph in text.split("\n\n"):
                if not paragraph.strip():
                    continue
                meta = ChunkMetadata(
                    source=path,
                    page=page_num,
                    section="",
                    topics=topics,
                    level="concept",
                    part_candidates=part_candidates,
                    created_at=datetime.utcnow().isoformat(),
                )
                chunks.append((paragraph, meta))
    vs = VectorStore()  # 벡터 DB 클라이언트
    vs.add_documents(chunks)
```


***

## 10. RAGStore 인터페이스 \& 구현 (relevance-checker-module.md 포함)

### 10.1 RAGStore 인터페이스

```python
# /03_llm_rag_agents/rag/store.py

from typing import List, Dict, Any, Tuple
from .schema import ChunkMetadata

class RAGStore:
    def search(self, query: str, filters: Dict[str, Any], k: int) -> List[Tuple[str, ChunkMetadata]]:
        raise NotImplementedError

    def add_documents(self, docs: List[Tuple[str, ChunkMetadata]]) -> None:
        raise NotImplementedError

    def reindex(self, new_docs: List[Tuple[str, ChunkMetadata]]) -> None:
        raise NotImplementedError
```


### 10.2 Relevance Checker Runnable[^4]

```python
# /03_llm_rag_agents/rag/relevance_checker.py

from typing import Dict, Any
from ..llm_layer import llm_call

RELEVANCE_SYSTEM_PROMPT = """
You are a relevance checker for a book-writing RAG system.
Given a question and a context, decide if the context is truly useful.
Return JSON: {"is_relevant": bool, "score": float, "rationale": "..." }.
"""

async def check_relevance(question: str, context: str, run_id: str, node_id: str) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": RELEVANCE_SYSTEM_PROMPT},
        {"role": "user", "content": f"Question:\n{question}\n\nContext:\n{context}"},
    ]
    resp = await llm_call(
        agent_role="auto_critic",
        messages=messages,
        run_id=run_id,
        node_id=node_id,
        temperature=0.0,
    )
    content = resp["choices"][^0]["message"]["content"]
    # JSON 파싱 로직 필요(try/except + fallback)
    import json
    return json.loads(content)
```


### 10.3 LangGraph에서의 RAG + Relevance 라우팅[^12]

```python
# /03_llm_rag_agents/rag/graph_nodes.py

from .store import RAGStore
from .relevance_checker import check_relevance
from ..states import ChapterState

async def retrieve_with_relevance(state: ChapterState, run_id: str, node_id: str) -> ChapterState:
    question = f"{state['title']} - {state['purpose']}"
    filters = {"part_candidates": [state["part_id"]]} if state.get("part_id") else {}
    store = RAGStore()
    candidates = store.search(question, filters=filters, k=10)

    relevant_notes = []
    citations = []
    for text, meta in candidates:
        res = await check_relevance(question, text, run_id, node_id)
        if res["is_relevant"] and res["score"] >= 0.6:
            relevant_notes.append({"text": text, "meta": meta.dict(), "relevance": res})
            citations.append(f"{meta.source}_p{meta.page}")

    state["research_notes"] = relevant_notes
    state["rag_citations"] = citations
    return state
```


***

## 11. RAG + Agent 통합 패턴 (rag-agent-integration-patterns.md)

### 11.1 표준 패턴

- Retrieval → Relevance → Summarization → Planning/Generation.[^2][^14]
- BAAS에서는 **Chapter Graph**에서 다음 구조 사용:
    - `research` 노드: RAG + Relevance + note 생성
    - `write` 노드: research_notes·outline 기반 초안
    - `eval` 노드: Auto Critic + 점수·피드백
    - 루프/종료: iteration/score 기준.


### 11.2 품질 평가 루프

- 각 실행에서 **question-context-answer-eval** 4요소를 구조화해 저장.[^10]
- 이후:
    - Recall/Precision 기반 통계
    - 프롬프트/임계값 튜닝
    - 지식 인덱스 보강.

```python
# /03_llm_rag_agents/eval/log_schema.py

class RAGEvalRecord(BaseModel):
    id: str
    question: str
    context_snippets: List[str]
    answer: str
    eval_score: float
    eval_feedback: str
    created_at: datetime
```


***

## 12. 체크리스트 – LLM · RAG · Agentic Layer

- [ ] 역할별 모델 매핑·OpenRouter 구성·공통 LLM 레이어가 구현되어 있는가.[^1]
- [ ] developer/system/user/assistant/tool 역할 프롬프트 아키텍처와 템플릿이 명시되어 있는가.[^9][^8]
- [ ] 모든 주요 에이전트(Book Supervisor, Outline Planner, Research/Case/Writer/Style/Auto Critic)가 역할/입출력/프롬프트를 갖고 있는가.[^15][^3]
- [ ] RAG 파이프라인(PDF→청크→임베딩→벡터DB→검색→관련성체커)이 구현되어 있는가.[^4][^2]
- [ ] Relevance Checker 모듈이 LangChain Runnable/노드로 존재하며, LangGraph 라우팅에 통합되어 있는가.[^4][^12]
- [ ] RAG + Agent 통합 패턴에서 품질 평가 루프(질문·문맥·응답·평가)가 데이터로 축적되고 있는가.[^10]

***

이 백서는 디렉터리 3: **LLM · RAG · Agentic Layer**를 기준으로, BAAS의 “생각하는 레이어”를 **역할 정의 → 모델 라우팅 → 프롬프트 구조 → RAG 인프라 → Relevance Checker → LangGraph 통합**까지 끊김 없이 연결할 수 있도록 구성했습니다.[^3][^2][^1][^4]

레포에서 실제로 구현할 때는, 이 문서의 코드 블록을 다음 경로들로 분할하면 됩니다:

- `/03_llm_rag_agents/llm_router.py`
- `/03_llm_rag_agents/openrouter_client.py`
- `/03_llm_rag_agents/llm_layer.py`
- `/03_llm_rag_agents/states.py`
- `/03_llm_rag_agents/prompts/...`
- `/03_llm_rag_agents/rag/schema.py`, `store.py`, `ingest_pdf.py`, `relevance_checker.py`, `graph_nodes.py`
- `/03_llm_rag_agents/eval/log_schema.py`

원하시면 다음 턴에서, 특정 부분(예: **멀티에이전트 설계 전체 코드** 또는 **RAG 인덱싱/검색 모듈 전체 코드**)만 골라 훨씬 더 디테일한 “실행 가능한 코드 전체”를 이어서 작성할 수 있습니다.

<div align="center">⁂</div>

[^1]: https://peliqan.io/blog/langchain-vs-langgraph/

[^2]: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/

[^3]: https://langchain-ai.github.io/langgraph/concepts/multi_agent/

[^4]: https://wikidocs.net/267810

[^5]: https://vectorize.io/blog/designing-agentic-ai-systems-part-1-agent-architectures

[^6]: https://www.invent.ai/blog/key-components-of-agentic-ai-architecture-building-the-foundation

[^7]: https://blog.langchain.com/langgraph-multi-agent-workflows/

[^8]: https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case/leveraging-system-user-and-assistant-roles-for-better-prompts

[^9]: https://practiqai.com/blog/system-prompts-roles-instruction-hierarchy

[^10]: https://www.clarifai.com/blog/agentic-prompt-engineering

[^11]: https://docs.nvidia.com/nim/large-language-models/latest/system-example.html

[^12]: https://www.swarnendu.de/blog/langgraph-best-practices/

[^13]: https://blog.langchain.com/building-langgraph/

[^14]: https://www.siddharthbharath.com/build-deep-research-agent-langgraph/

[^15]: https://www.codersarts.com/post/a-complete-guide-to-creating-a-multi-agent-book-writing-system-part-3

