# 모노레포 구조 및 환경 설정 (Monorepo Structure and Env)

## 2.1 디렉터리 구조
- **apps/**: `web` (Next.js), `api` (FastAPI), `worker` (배치/리서치).
- **packages/**: `core`, `llm_rag`, `workflows`, `ui`, `prompts`.

## 2.2 환경 변수 관리
- `.env.example` 파일을 기반으로 환경별(`.env.dev`, `.env.prod`) 설정 분리.
- 주요 키: `OPENROUTER_API_KEY`, `SUPABASE_URL`, `VECTOR_DB_URL`.
