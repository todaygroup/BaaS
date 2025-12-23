# 프롬프트 역할 및 지시 계층 (Prompt Roles and Instruction Hierarchy)

## 4.1 5가지 표준 역할
1. **Developer**: 시스템 동작 원칙 (헌법).
2. **System**: 현재 상태, 컨텍스트, RAG 정보.
3. **User**: 구체적인 저자 지시사항.
4. **Assistant**: AI의 응답 기록.
5. **Tool**: 검색 결과 등 외부 데이터 전달.

## 4.2 계층 구조
- 지시사항이 충돌할 경우: **Developer > User > System** 순으로 우선순위 부여.
