from typing import Dict, Any, Optional
import json
from ..llm.layer import llm_call

RELEVANCE_SYSTEM_PROMPT = """
You are a relevance checker for a book-writing RAG system.
Given a question and a context, decide if the context is truly useful.
Return JSON ONLY: {"is_relevant": bool, "score": float, "rationale": "..." }.
"""

async def check_relevance(question: str, context: str, run_id: str, node_id: str) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": RELEVANCE_SYSTEM_PROMPT},
        {"role": "user", "content": f"Question:\n{question}\n\nContext:\n{context}"},
    ]
    resp = await llm_call(
        agent_role="auto_critic",
        messages=messages,
        run_id=run_id,
        node_id=node_id,
        temperature=0.0,
    )
    
    content = resp["choices"][0]["message"]["content"]
    
    # Simple JSON extraction (in case of markdown blocks)
    try:
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        return json.loads(content)
    except Exception as e:
        print(f"[RELEVANCE ERROR] Failed to parse JSON: {e}")
        return {"is_relevant": False, "score": 0.0, "rationale": f"Parsing error: {str(e)}"}
