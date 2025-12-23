from enum import Enum
from typing import Literal, Dict, Any

class Role(str, Enum):
    SUPERVISOR = "book_supervisor"
    PLANNER = "outline_planner"
    RESEARCHER = "research_agent"
    CASE_STUDY = "case_study_agent"
    WRITER = "chapter_writer"
    CONSISTENCY = "structure_consistency_agent"
    STYLE = "style_localization_agent"
    CRITIC = "auto_critic"
    MARKETING = "marketing_agent"

AgentRole = Role

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
