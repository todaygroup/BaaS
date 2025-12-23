<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 지금까지 나눈 대화를 심층 분석하여 **Book-Authoring Agent System (BAAS)** 내용을 작성할 때 각 권 별로 백서 형태로 하나씩 문서를 생성합니다. 문서를 작성하기 전에 모든 내용을 "제 1 원칙 사고법"을 기준으로 하여 전 과정을 근본적인 본질에서 시작하여 요약본 형태가 아니라 모든 내용이 하나도 빠짐없이 필요한 모든 단계가 순차적으로 적용된 Full Stack 문서 형태로 작성합니다.

"디렉터리 5: UX · Interaction · Ops Runbook" 에 대한 내용을 실제 책 분량 수준으로 더 확장해서 각 권 별로 작성합니다. 이때 실 구현을 위한 코드·템플릿을 상세화하는 과정을 포함하여 모든 소스코드가 포함되도록 작성합니다.

디렉터리 5는 BAAS를 “실제 사람이 매일 쓰는 서비스”로 만들기 위한 **UX / 상호작용 / 관찰성 / 운영 Runbook**의 풀스택 레이어입니다. 아래는 한 권짜리 백서 수준으로 설계한 “Guide 5 – UX · Interaction · Ops Runbook for BAAS”의 구조와 핵심 내용·코드 스캐폴드입니다.[^1][^2][^3]

***

# Guide 5. UX · Interaction · Ops Runbook for BAAS

**Book-Authoring Agent System (BAAS) – UX·상호작용·관찰성·운영 백서**

***

## 1. 제1원칙: BAAS UX의 본질

### 1.1 BAAS UX가 풀어야 할 문제

- BAAS의 작업은 **30초~수분 단위의 장기 LLM/에이전트 실행**이 많다.[^4][^2]
- 사용자는 “에이전트가 실제로 일을 하고 있고, 그 결과가 가치가 있다”는 확신이 있어야 기다린다.[^2]
- 따라서 UX의 본질은:
    - **상태·진행 상황·가치**를 계속 투명하게 보여주고,
    - **중단/재시작/백그라운드 전환** 같은 제어권을 사용자에게 주는 것.[^5][^2]


### 1.2 UX · Interaction · Ops 계층 분리

- UX Layer: 화면 구조, 플로우, 컴포넌트, 프롬프트 UX.
- Interaction Layer: 프론트–백간 상태 동기화, 스트리밍/폴링, 재시작/취소.[^6][^1]
- Ops Layer: 로그/트레이스/알람, Runbook, 거버넌스.[^3][^7]

***

## 2. UX 원칙 \& 네비게이션 (ux-principles-and-navigation.md)

### 2.1 UX 원칙

- **원칙 1 – 상태 가시성**: “지금 시스템이 무엇을 하고 있는지” 항상 한 줄로 설명 가능해야 한다.[^2]
- **원칙 2 – 예측 가능한 결과**: 동일한 버튼·동일한 설정 → 비슷한 결과.
- **원칙 3 – 기다림의 가치 설명**: “30초 기다리는 동안 무슨 일이 벌어지는지” 설명.[^2]
- **원칙 4 – 히스토리 \& 재현성**: 이전 실행 결과·버전 비교를 쉽게.[^1]


### 2.2 네비게이션 모델

- 상위 모드:
    - Dashboard
    - Book Overview
    - Chapter Workspace
    - Execution \& Debugging
    - Settings \& Integrations

```ts
// /05_ux_interaction_ops/routes.ts
export const routes = {
  dashboard: "/",
  workspace: (ws: string) => `/workspaces/${ws}`,
  project: (ws: string, proj: string) => `/workspaces/${ws}/projects/${proj}`,
  book: (ws: string, proj: string, book: string) =>
    `/workspaces/${ws}/projects/${proj}/books/${book}`,
  chapter: (ws: string, p: string, b: string, c: string) =>
    `/workspaces/${ws}/projects/${p}/books/${b}/chapters/${c}`,
  executions: (ws: string, p: string, b: string) =>
    `/workspaces/${ws}/projects/${p}/books/${b}/executions`,
};
```


***

## 3. 화면 설계 \& 컴포넌트 (wireframes-*.md)

### 3.1 Dashboard – “지금 무슨 일이 어디서 진행 중인가?”

#### 3.1.1 주요 섹션

- 최근 실행(Last Runs) – 그래프 타입/책/챕터/상태/시간.
- 진행 중 작업(In Progress) – ETA/단계/취소/백그라운드 버튼.[^2]
- 프로젝트/책 카드 – 상태 요약, “다음 액션” CTA.

```tsx
// /05_ux_interaction_ops/components/dashboard/DashboardPage.tsx
"use client";

import { useQuery } from "@tanstack/react-query";
import { ExecutionCard } from "./ExecutionCard";
import { BookCard } from "./BookCard";

export function DashboardPage() {
  const { data: executions } = useQuery({
    queryKey: ["recent-executions"],
    queryFn: fetchRecentExecutions,
    refetchInterval: 5000,
  });

  const { data: books } = useQuery({
    queryKey: ["recent-books"],
    queryFn: fetchRecentBooks,
  });

  return (
    <div className="space-y-4 p-4">
      <section>
        <h2 className="text-lg font-semibold mb-2">진행 중 작업</h2>
        <div className="grid gap-2 md:grid-cols-2">
          {executions?.in_progress.map((ex: any) => (
            <ExecutionCard key={ex.id} execution={ex} />
          ))}
        </div>
      </section>
      <section>
        <h2 className="text-lg font-semibold mb-2">책 프로젝트</h2>
        <div className="grid gap-4 md:grid-cols-3">
          {books?.map((book: any) => (
            <BookCard key={book.id} book={book} />
          ))}
        </div>
      </section>
    </div>
  );
}
```


### 3.2 Chapter Workspace – “단일 챕터의 BAAS 조종석”

#### 3.2.1 레이아웃 영역

- 왼쪽: Graph Timeline (노드 순서, 상태, 시간).
- 오른쪽: Draft Viewer + Eval Score + Action Bar.
- 상단: “Run/Retry/Stop” 버튼 및 상태 설명.

```tsx
// /05_ux_interaction_ops/components/chapter/ChapterWorkspace.tsx
"use client";

import { useQuery, useMutation } from "@tanstack/react-query";
import { Button } from "@/components/ui/button";
import { ChapterGraphTimeline } from "./ChapterGraphTimeline";
import { ChapterDraftViewer } from "./ChapterDraftViewer";

export function ChapterWorkspace({ chapterId, bookId }: { chapterId: string; bookId: string }) {
  const { data: execution, refetch } = useQuery({
    queryKey: ["chapter-execution", chapterId],
    queryFn: () => fetchChapterExecution(chapterId),
    refetchInterval: 3000,
  });

  const runMutation = useMutation({
    mutationFn: () => runChapterGraph({ chapterId, bookId }),
    onSuccess: () => refetch(),
  });

  const stopMutation = useMutation({
    mutationFn: () => stopChapterGraph(execution?.run_id),
    onSuccess: () => refetch(),
  });

  return (
    <div className="flex h-full">
      <div className="w-1/2 border-r">
        <ChapterGraphTimeline execution={execution} />
      </div>
      <div className="w-1/2 flex flex-col">
        <div className="p-2 border-b flex items-center justify-between">
          <div>
            <h2 className="font-semibold">챕터 초안</h2>
            <p className="text-xs text-muted-foreground">
              {execution?.status === "running"
                ? "에이전트가 챕터를 작성 중입니다. 평균 30~90초 소요됩니다."
                : "마지막 실행 결과입니다."}
            </p>
          </div>
          <div className="space-x-2">
            <Button
              variant="outline"
              onClick={() => stopMutation.mutate()}
              disabled={!execution || execution.status !== "running"}
            >
              중단
            </Button>
            <Button onClick={() => runMutation.mutate()} disabled={runMutation.isPending}>
              {runMutation.isPending ? "실행 중..." : "챕터 그래프 실행"}
            </Button>
          </div>
        </div>
        <div className="flex-1 overflow-auto">
          <ChapterDraftViewer execution={execution} />
        </div>
      </div>
    </div>
  );
}
```


***

## 4. Prompt UX \& Vibe Coding Playbook (vibe-coding-workflow.md, prompt-ux-patterns.md, prompt-playbooks.md)

### 4.1 BAAS용 Vibe Coding 플로우[^8][^9][^6]

- Describe → Plan → Scaffold → Refine → Test → Document
- BAAS에서는:
    - Describe: 책/챕터 요구사항 입력 화면(주제·독자·톤·사례 수준 등).
    - Plan: Outline Planner 실행 + 구조 UI.
    - Scaffold: Chapter Graph/Book Graph 코드 스캐폴드(LLM 에이전트 관점).
    - Refine: Auto Critic/편집.
    - Test: AgentEval/독자 관점 피드백.
    - Document: 결과 Export + 내부 문서 자동화.


### 4.2 Prompt UX – 입력 컴포넌트 설계

```tsx
// /05_ux_interaction_ops/components/book/BookPromptForm.tsx
"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export function BookPromptForm({ onSubmit }: { onSubmit: (payload: any) => void }) {
  const [topic, setTopic] = useState("");
  const [audience, setAudience] = useState("");
  const [tone, setTone] = useState("전략적이지만 친근한 한국어");
  const [objectives, setObjectives] = useState("");

  return (
    <form
      className="space-y-4"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ topic, audience, tone, objectives });
      }}
    >
      <div>
        <label className="block text-sm font-medium">책 주제</label>
        <Textarea
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="예: Agentic AI를 활용한 B2B 세일즈 전략"
        />
      </div>
      <div>
        <label className="block text-sm font-medium">주요 독자</label>
        <Textarea
          value={audience}
          onChange={(e) => setAudience(e.target.value)}
          placeholder="예: 한국어를 사용하는 B2B 스타트업 대표 및 세일즈 리더"
        />
      </div>
      <div>
        <label className="block text-sm font-medium">톤/스타일</label>
        <Textarea
          value={tone}
          onChange={(e) => setTone(e.target.value)}
          placeholder="예: 전략 리포트 느낌이면서도 친근한 말투"
        />
      </div>
      <div>
        <label className="block text-sm font-medium">특별히 달성하고 싶은 목표</label>
        <Textarea
          value={objectives}
          onChange={(e) => setObjectives(e.target.value)}
          placeholder="예: 실제 현업 팀이 바로 적용 가능한 프레임워크와 체크리스트 제공"
        />
      </div>
      <Button type="submit" className="w-full">
        아웃라인 생성 요청
      </Button>
    </form>
  );
}
```

이 폼에서 받은 입력은 “Describe” 역할을 하고, 내부적으로는 Guide 3에서 정의한 **Book Planner 프롬프트**에 맵핑된다.[^10][^8]

### 4.3 Prompt Playbook – 예시 템플릿

```md
<!-- /05_ux_interaction_ops/prompt-playbooks/write-chapter.md -->
# Write Chapter Prompt Template v1.0

## Developer Role
- BAAS 전역 규칙(developer prompt) 포함.

## System Role
- [BOOK METADATA], [CHAPTER METADATA], [RAG SUMMARY] 블록 포함.

## User Role
- 책 주제, 독자, 톤, 챕터 목적을 다시 한번 요약.
- 구조/분량/스타일 제약 명시.
- 출력 형식(Heading/Markdown/JSON) 명시.

## Example Input
...

## Example Output
...
```


***

## 5. Observability \& Logging (observability-and-logging.md)

### 5.1 LLM/에이전트용 로그 스키마[^11][^12][^3]

```python
# /05_ux_interaction_ops/observability/log_schema.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LLMCallLog(BaseModel):
  trace_id: str
  run_id: str
  node_id: str
  agent_role: str
  model: str
  provider: str
  created_at: datetime
  latency_ms: int
  input_tokens: int
  output_tokens: int
  status: str
  error: Optional[str] = None

class GraphRunLog(BaseModel):
  run_id: str
  graph_type: str
  book_id: Optional[str]
  chapter_id: Optional[str]
  status: str
  started_at: datetime
  finished_at: Optional[datetime]
```


### 5.2 로그 기록 함수

```python
# /05_ux_interaction_ops/observability/logger.py

import json
from datetime import datetime
from .log_schema import LLMCallLog, GraphRunLog

LOG_FILE = "logs/llm_calls.jsonl"
RUN_FILE = "logs/graph_runs.jsonl"

def log_llm_call(**kwargs):
    log = LLMCallLog(
        created_at=datetime.utcnow(),
        provider="openrouter",
        **kwargs,
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log.json(ensure_ascii=False) + "\n")

def log_graph_run(**kwargs):
    log = GraphRunLog(**kwargs)
    with open(RUN_FILE, "a", encoding="utf-8") as f:
        f.write(log.json(ensure_ascii=False) + "\n")
```

- 실제 서비스에서는 OpenTelemetry + Prometheus/Grafana/전용 LLM Observability 솔루션과 연동.[^3][^11]

***

## 6. AI Evaluation \& Feedback Loops (ai-evaluation-and-feedback-loops.md)

### 6.1 AgentEval 결과 UX

- Chapter Workspace에 `eval_score`와 `eval_feedback`을 시각적으로 보여주고, “재생성/수정 필요” 여부를 강조.[^13][^14]

```tsx
// /05_ux_interaction_ops/components/chapter/ChapterEvalBadge.tsx
export function ChapterEvalBadge({ score }: { score: number | null }) {
  if (score == null) return <span className="text-xs text-muted-foreground">미평가</span>;
  const color =
    score >= 0.8 ? "bg-emerald-100 text-emerald-800" :
    score >= 0.6 ? "bg-amber-100 text-amber-800" :
    "bg-red-100 text-red-800";
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${color}`}>
      Eval {score.toFixed(2)}
    </span>
  );
}
```


***

## 7. AI 거버넌스 \& 위험 관리 (ai-governance-and-risk.md)

### 7.1 정책 \& 변경 관리[^7][^15][^3]

- 모델/프롬프트/그래프/RAG 인덱스 버전별로 **정책·역할·책임** 정의.
- 중대한 변경(모델 교체, 프롬프트 대폭 수정)은:
    - Shadow 테스트
    - Canary 릴리즈
    - Runbook 기반 모니터링.

***

## 8. Ops Runbook \& 확장 시나리오 (operations-runbook.md, evolution-scenarios.md)

### 8.1 Runbook 기본 템플릿[^13][^7]

```md
# Incident Runbook: Chapter Graph Failure

## 1. 증상
- 사용자가 "챕터 그래프 실행" 후 5분이 지나도 결과 없음
- Dashboard에 특정 run_id가 'running' 상태로 멈춤

## 2. 점검 순서
1. Observability 대시보드에서 run_id 검색
2. NodeRun 로그 확인: 마지막 성공 노드, 에러 노드
3. LLMCallLog에서 에러 발생 지점 확인 (rate limit, timeout 등)
4. RAGStore 상태 확인 (벡터DB 연결 여부)

## 3. 즉각 조치
- 장애 원인이 명확할 경우: 재시도 또는 fallback 플로우 실행
- 원인 불명일 경우: 해당 run 종료 + 사용자에게 알림(실패 원인·다음 조치 안내)

## 4. 사후 조치
- 원인 분석 후 Graph/Prompt/RAG 튜닝
- Runbook 업데이트
```


### 8.2 확장 시나리오

- **기능 확장**: 새 챕터 타입(워크북, 연습문제) 에이전트 추가.
- **성능 확장**: 멀티 리전 배포, 캐싱, LLM Gateway 최적화.[^5][^13]
- **조직 확장**: 멀티테넌시 강화, 엔터프라이즈 권한 모델 추가.

***

## 9. 디렉터리 5 체크리스트

- [ ] Dashboard/Book/Chapter/Execution/Settings 화면이 “지금 시스템이 무엇을 하고 있는지”를 명확히 보여주는가.[^16][^2]
- [ ] BAAS용 Prompt UX가 Describe→Plan→Scaffold→Refine→Test→Document 흐름을 자연스럽게 지원하는가.[^8][^6]
- [ ] LLM/그래프/에이전트 호출에 대한 로그·메트릭·트레이스가 통합된 스키마로 수집되고 있는가.[^12][^11][^3]
- [ ] AgentEval/유저 피드백을 품질 개선 루프로 연결하는 메커니즘이 있는가.[^14][^7]
- [ ] LLM·RAG·에이전트 변경에 대한 거버넌스/리스크 관리 프로세스가 수립되어 있는가.[^15][^3]
- [ ] 주요 장애 유형별 Runbook이 정의되어 있고, 실제 운영에서 사용 가능한가.[^7][^13]

***

이 Guide 5는 디렉터리 5: **UX · Interaction · Ops Runbook**을 기준으로 BAAS를 “실제 저자가 매일 사용하는 서비스”로 만들기 위한 UX 패턴·프론트 코드·프롬프트 UX·관찰성·Runbook까지 연결하는 풀스택 설계입니다.[^1][^3][^2]

레포에서는:

- `/05_ux_interaction_ops/components/...`
- `/05_ux_interaction_ops/observability/...`
- `/05_ux_interaction_ops/prompt-playbooks/...`
- `/05_ux_interaction_ops/runbooks/...`

로 나누어 배치하고, 이전 Guide 1~4에서 정의한 스택과 연결하면 전체 BAAS 백서 세트가 완성됩니다.
<span style="display:none">[^17][^18][^19][^20][^21][^22]</span>

<div align="center">⁂</div>

[^1]: https://eugeneyan.com/writing/llm-patterns/

[^2]: https://particula.tech/blog/long-running-ai-tasks-user-interface-patterns

[^3]: https://petronellatech.com/blog/monitor-secure-scale-the-enterprise-playbook-for-llm-observability/

[^4]: https://developer.atlassian.com/platform/forge/llm-long-running-process-with-forge-realtime/

[^5]: https://focused.io/lab/trends-and-patterns-for-creating-a-custom-llm-app

[^6]: https://www.gocodeo.com/post/prompt-ux-in-vibe-coding-a-new-frontier-for-software-design

[^7]: https://galileo.ai/blog/understanding-llm-observability

[^8]: https://emergent.sh/learn/vibe-coding-prompts

[^9]: https://uxdesign.cc/cracking-the-code-of-vibe-coding-124b9288e551

[^10]: https://strapi.io/blog/vibe-coding-prompt-techniques

[^11]: https://apxml.com/courses/mlops-for-large-models-llmops/chapter-5-llm-monitoring-observability-maintenance/llm-logging-observability

[^12]: https://skywork.ai/blog/llm-observability-best-practices-haiku-logging-tracing-guardrails/

[^13]: https://www.logicmonitor.com/blog/ai-observability

[^14]: https://www.clarifai.com/blog/agentic-prompt-engineering

[^15]: https://practiqai.com/blog/system-prompts-roles-instruction-hierarchy

[^16]: https://blog.logrocket.com/designing-llm-first-products/

[^17]: https://arxiv.org/html/2507.04469v1

[^18]: https://dev.to/dmitryame/design-smarter-testing-top-llms-for-mobile-interface-optimization-k89

[^19]: https://www.francescatabor.com/articles/2025/9/6/ux-design-without-designers-how-llms-are-rewriting-ui-in-real-time

[^20]: https://uxdesign.cc/thinking-past-the-cliche-of-llms-ai-design-patterns-c9b849fce9e8

[^21]: https://www.reddit.com/r/ClaudeAI/comments/1kivv0w/the_ultimate_vibe_coding_guide/

[^22]: https://lantern.splunk.com/Observability_Use_Cases/Troubleshoot/Automating_alert_investigations_by_integrating_LLMs_with_the_Splunk_platform_and_Confluence

