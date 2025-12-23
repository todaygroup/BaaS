# LLM 레이어 아키텍처 (LLM Layer Architecture)

## 3.1 공통 호출 레이어
- Role → Model 매핑 자동화.
- 로깅, 재시도, 토큰 추적 통합.

## 3.2 OpenRouter 클라이언트 예시
```python
class OpenRouterClient:
    async def chat(self, messages: list, role: str):
        model = ROLE_MODEL_MAP.get(role, "gpt-4o-mini")
        # API call with headers
        # return response
```
- 모든 에이전트 노드는 이 공통 레이어를 통해 LLM과 통신함.
