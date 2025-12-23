# LLM 프로바이더 전략 (LLM Provider Strategy)

## 2.1 OpenRouter 기반 게이트웨이
- 다양한 모델(GPT-4o, Claude 3.5, Gemini 1.5 Pro 등)을 단일 API로 접근.
- 비용 및 성능 최적화를 위한 역할별 모델 매핑.

## 2.2 역할별 모델 매핑
- **Planner/Writer**: GPT-4o (고성능)
- **Reviewer/Supervisor**: GPT-4o-mini (효율성)
- **Research**: Claude 3.5 Sonnet (추론/분석력)

```python
ROLE_MODEL_MAP = {
    "outline_planner": "openai/gpt-4o",
    "chapter_writer": "openai/gpt-4o",
    "auto_critic": "openai/gpt-4o-mini",
    "research_agent": "anthropic/claude-3.5-sonnet"
}
```
