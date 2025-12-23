from typing import Literal, Dict, Any

AgentRole = Literal[
    "book_supervisor",
    "outline_planner",
    "research_agent",
    "case_study_agent",
    "chapter_writer",
    "structure_consistency_agent",
    "style_localization_agent",
    "auto_critic",
    "marketing_agent",
]

ROLE_MODEL_MAP: Dict[AgentRole, Dict[str, Any]] = {
    "book_supervisor": {"model": "openai/gpt-4o-mini", "temperature": 0.3},
    "outline_planner": {"model": "openai/gpt-4o", "temperature": 0.4},
    "research_agent": {"model": "anthropic/claude-3.5-sonnet", "temperature": 0.2},
    "case_study_agent": {"model": "openai/gpt-4o", "temperature": 0.7},
    "chapter_writer": {"model": "openai/gpt-4o", "temperature": 0.5},
    "structure_consistency_agent": {"model": "openai/gpt-4o-mini", "temperature": 0.2},
    "style_localization_agent": {"model": "openai/gpt-4o", "temperature": 0.4},
    "auto_critic": {"model": "openai/gpt-4o-mini", "temperature": 0.1},
    "marketing_agent": {"model": "openai/gpt-4o", "temperature": 0.7},
}

ENV_MODEL_DEFAULTS = {
    "dev": {
        "default": "openai/gpt-4o-mini",
        "fallback": "openai/gpt-4o-mini", # Simplified for now
    },
    "prod": {
        "default": "openai/gpt-4o",
        "fallback": "openai/gpt-4o-mini",
    },
}
