# 기술 스택 및 제약 (Tech Stack and Constraints)

## 2.1 코어 스택 선택
- **언어/런타임**: Python 3.10+, TypeScript 5+ (Next.js)
- **Agentic 오케스트레이션**: LangGraph, LangChain Core
- **LLM & Provider**: OpenRouter (GPT-4o, Claude 3.5 Sonnet 등)
- **데이터**: Supabase (Postgres), Qdrant 또는 Pinecone (VectorDB)
- **백엔드**: FastAPI
- **프론트엔드**: Next.js 14 (App Router)
- **관찰성**: OpenTelemetry, JSONL 구조화 로그

## 2.2 제약 조건
- **비용**: 챕터당 LLM 비용 200~500원 수준 목표.
- **품질**: AgentEval 점수 ≥ 0.8 (출판 가능한 수준).
- **팀**: 소규모 팀으로 운영 가능한 신규 시스템 아키텍처.
