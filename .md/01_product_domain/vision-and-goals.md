# 비전 및 목표 (Vision and Goals)

## 2.1 비전 선언문(Vision Statement)

> “BAAS는 한 사람의 저자가 수년간 쌓아온 지식과 스타일을 AI 에이전트 팀에 이식하여, **책 한 권 전체를 고품질로 자동 집필**할 수 있게 만드는 지적 생산 인프라이다.”

### 핵심 키워드:
- **Author-Centric**: 저자의 고유 관점/스타일이 중심.
- **Agentic**: 다중 에이전트 팀이 협업해 완성.
- **Reusable Knowledge**: 한 번 구축한 지식·워크플로우로 여러 책/콘텐츠 생산.

## 2.2 목적(Goals)
- **G1. 시간 단축**: 책 한 권 집필 시간을 기존 대비 80% 이상 단축.
- **G2. 품질 유지/개선**: Auto Critic + Human Review를 통해 기존 저서 대비 동등 이상 품질 유지.
- **G3. 확장성**: 동일 시스템으로 저자 1명 → 저자 여러 명, 단행본 → 시리즈/교재/워크북까지 확장 가능.

## 2.3 North Star Metric & KPI
- **NSM**: “BAAS를 사용해 **완성된 원고(80% 이상 Human 편집 완료 상태)**로 통합된 책 권수 / 저자 수”
- **KPI**: 챕터당 평균 생성 시간, 챕터당 평균 수정 비율, AgentEval 평균 점수 등.

```yaml
# vision-and-goals.example.yml
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
