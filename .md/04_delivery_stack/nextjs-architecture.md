# Next.js 아키텍처 (Next.js Architecture)

## 4.1 프로젝트 구조
- **app/**: App Router 기반 페이지 구성 (`dashboard/`, `workspaces/`, `projects/`).
- **components/**: 아토믹 디자인 또는 도메인별 컴포넌트 분리 (`layout/`, `chapter/`, `book/`).
- **lib/**: API 클라이언트 및 유틸리티.

## 4.2 주요 라우팅
- `/workspaces/[wsId]/projects/[pId]/books/[bId]`: 책 대시보드.
- `/workspaces/[wsId]/projects/[pId]/books/[bId]/chapters/[cId]`: 챕터 편집 및 에이전트 워크스페이스.
