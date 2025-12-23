# 요구사항 (Requirements)

## 6.1 기능 요구사항
- **새 책 기획**: 주제, 독자, 톤 기반 아웃라인 생성.
- **챕터 작성 플로우**: planned → researching → drafted → revising → final.
- **에이전트 매핑**: researching(Research Agent + RAG), drafted(Chapter Writer), revising(Auto Critic).

## 6.2 비기능 요구사항
- 성능: 챕터 생성 1~2분 이내.
- 품질: AgentEval 점수 ≥ 0.75.
- 보안: 워크스페이스 단위 RAG 인덱스 격리.
