# Guide 3. LLM · RAG · Agentic Layer for BAAS

**Book-Authoring Agent System (BAAS) – LLM·RAG·에이전트 레이어 백서**

---

## 1. 개요
이 문서는 BAAS의 지능 레이어(LLM, RAG, 멀티에이전트)에 대한 상세 설계 및 구현 가이드를 제공합니다.

## 2. 세부 문서 목록
- [LLM Provider & OpenRouter 전략](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/llm-provider-strategy.md)
- [LLM 레이어 아키텍처](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/llm-layer-architecture.md)
- [프롬프트 역할 & 지시 계층](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/prompt-roles-and-instruction-hierarchy.md)
- [프롬프트 템플릿 & 패턴](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/prompt-templates-and-patterns.md)
- [프롬프트 라이브러리 구조](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/prompt-library-structure.md)
- [멀티에이전트 아키텍처](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/multi-agent-architecture.md)
- [에이전트 패턴 & 베스트 프랙티스](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/agent-patterns-and-best-practices.md)
- [데이터 & RAG 인프라](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/data-rag-infra.md)
- [Relevance Checker 모듈](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/relevance-checker-module.md)
- [RAG + Agent 통합 패턴](file:///c:/Users/SEC/.gemini/antigravity/scratch/baas/.md/03_agentic_layer/rag-agent-integration-patterns.md)

## 3. LLM · RAG · Agentic Layer 체크리스트
- [ ] 역할별 모델 매핑·OpenRouter 구성·공통 LLM 레이어가 구현되어 있는가.
- [ ] developer/system/user/assistant/tool 역할 프롬프트 아키텍처와 템플릿이 명시되어 있는가.
- [ ] 모든 주요 에이전트(Book Supervisor, Outline Planner, Research/Case/Writer/Style/Auto Critic)가 역할/입출력/프롬프트를 갖고 있는가.
- [ ] RAG 파이프라인(PDF→청크→임베딩→벡터DB→검색→관련성체커)이 구현되어 있는가.
- [ ] Relevance Checker 모듈이 LangChain Runnable/노드로 존재하며, LangGraph 라우팅에 통합되어 있는가.
- [ ] RAG + Agent 통합 패턴에서 품질 평가 루프(질문·문맥·응답·평가)가 데이터로 축적되고 있는가.
