# 관련성 체크 모듈 (Relevance Checker Module)

## 10.1 목적
- 검색된 RAG 결과가 현재 작업(챕터 작성 등)에 정말 유효한지 LLM으로 검증.
- 쓰레기 데이터(Noise)가 생성 품질을 저하시키는 것을 방지.

## 10.2 로직
- 입력: Question + Context Snippet.
- 출력: `{"is_relevant": bool, "score": float, "rationale": "..."}`.
- 점수 임계값(예: 0.6) 미만인 데이터는 프롬프트에서 제외.
