import os
from typing import Dict, Any, List
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

class OpenRouterClient:
    def __init__(self, agent_role: str, env: str = "prod"):
        from .router import ROLE_MODEL_MAP, ENV_MODEL_DEFAULTS
        self.agent_role = agent_role
        self.env = env
        self.model_config = ROLE_MODEL_MAP.get(agent_role, {"model": "openai/gpt-4o-mini", "temperature": 0.3})
        self.default_model = ENV_MODEL_DEFAULTS.get(env, ENV_MODEL_DEFAULTS["dev"])["default"]

    async def chat(self, messages: List[Dict[str, str]], **overrides: Any) -> Dict[str, Any]:
        payload = {
            "model": overrides.get("model") or self.model_config.get("model") or self.default_model,
            "messages": messages,
            "temperature": overrides.get("temperature", self.model_config.get("temperature", 0.3)),
        }
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://baas.ai", # Optional for OpenRouter
            "X-Title": "BAAS",
        }
        
        # In a real environment, we'd use a shared async client or handle retries
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(f"{OPENROUTER_BASE_URL}/chat/completions",
                                     json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()
