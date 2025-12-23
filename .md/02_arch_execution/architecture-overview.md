# 아키텍처 개요 (Architecture Overview)

## 3.1 C4 Level 1 – 시스템 컨텍스트
- **사용자(저자)** ↔ **BAAS Web UI (Next.js)** ↔ **BAAS API (FastAPI + LangGraph)**
- 외부 시스템: OpenRouter(LLM), Supabase(DB/Auth), Qdrant(VectorDB).

## 3.2 C4 Level 2 – 컨테이너
- `web`: Next.js 앱.
- `api`: FastAPI 서버 + LangGraph 런타임.
- `worker`: 배치 리서치 및 RAG 인덱싱 워커.
- `db`: Supabase.
- `vector`: 지식 저장을 위한 벡터 데이터베이스.
