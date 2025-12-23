from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END
from packages.llm_rag.src.agents.states import BookState

from packages.llm_rag.src.agents.planner import planner_agent

async def plan_outline_node(state: BookState) -> BookState:
    """Outline Planner Node implementation."""
    result = await planner_agent.plan_outline(
        topic=state.get("topic", "Untitled"),
        audience=state.get("audience", "General"),
        tone=state.get("tone", "Professional")
    )
    # Update state with generated outline
    state["outline"] = result["outline"]
    return state

def schedule_chapters_node(state: BookState) -> BookState:
    """Node to create chapter records based on outline."""
    return state

def create_book_graph():
    workflow = StateGraph(BookState)
    
    workflow.add_node("plan_outline", plan_outline_node)
    workflow.add_node("schedule_chapters", schedule_chapters_node)
    
    workflow.set_entry_point("plan_outline")
    workflow.add_edge("plan_outline", "schedule_chapters")
    workflow.add_edge("schedule_chapters", END)
    
    return workflow.compile()

book_graph = create_book_graph()
