from typing import Any, Dict, List, Optional
from time import perf_counter
from .client_openrouter import OpenRouterClient
from .router import Role

def mock_log_llm_call(**kwargs):
    print(f"[LLM LOG] {kwargs}", flush=True)

class LLMLayer:
    async def call_llm(
        self,
        role: Role,
        system_prompt: str,
        user_prompt: str,
        run_id: str = "manual",
        node_id: str = "manual",
        response_model: Optional[Any] = None,
        **overrides: Any,
    ) -> Dict[str, Any]:
        client = OpenRouterClient(role)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
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

llm_layer = LLMLayer()
