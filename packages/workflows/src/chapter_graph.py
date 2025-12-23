from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END
from packages.llm_rag.src.agents.states import ChapterState

def research_node(state: ChapterState) -> ChapterState:
    """Research Agent Node skeleton."""
    return state

def write_node(state: ChapterState) -> ChapterState:
    """Chapter Writer Node skeleton."""
    return state

def eval_node(state: ChapterState) -> ChapterState:
    """Auto Critic Node skeleton."""
    return state

def route_on_eval(state: ChapterState) -> str:
    if state.get("eval_score", 0) >= 0.8 or state.get("iteration", 0) >= 3:
        return END
    return "research"

def create_chapter_graph():
    workflow = StateGraph(ChapterState)
    
    workflow.add_node("research", research_node)
    workflow.add_node("write", write_node)
    workflow.add_node("eval", eval_node)
    
    workflow.set_entry_point("research")
    workflow.add_edge("research", "write")
    workflow.add_edge("write", "eval")
    workflow.add_conditional_edges("eval", route_on_eval, {END: END, "research": "research"})
    
    return workflow.compile()

chapter_graph = create_chapter_graph()
