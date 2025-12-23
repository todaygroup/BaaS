from typing import Any, Dict, List
from time import perf_counter
from .client_openrouter import OpenRouterClient

# Note: In a full implementation, this might call a global logging service
def mock_log_llm_call(**kwargs):
    print(f"[LLM LOG] {kwargs}")

async def llm_call(
    agent_role: str,
    messages: List[Dict[str, str]],
    run_id: str,
    node_id: str,
    **overrides: Any,
) -> Dict[str, Any]:
    client = OpenRouterClient(agent_role)
    t0 = perf_counter()
    try:
        resp = await client.chat(messages, **overrides)
        t1 = perf_counter()
        usage = resp.get("usage", {})
        
        mock_log_llm_call(
            run_id=run_id,
            node_id=node_id,
            model=resp.get("model", ""),
            latency_ms=int((t1 - t0) * 1000),
            input_tokens=usage.get("prompt_tokens", 0),
            output_tokens=usage.get("completion_tokens", 0),
            status="success",
        )
        return resp
    except Exception as e:
        t1 = perf_counter()
        mock_log_llm_call(
            run_id=run_id,
            node_id=node_id,
            model="unknown",
            latency_ms=int((t1 - t0) * 1000),
            input_tokens=0,
            output_tokens=0,
            status="error",
            error=str(e),
        )
        raise
