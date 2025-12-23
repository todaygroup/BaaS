from packages.workflows.src.chapter_graph import route_on_eval
from packages.llm_rag.src.agents.states import ChapterState

def test_route_on_eval_success():
    state: ChapterState = {"eval_score": 0.9, "iteration": 1}
    # END is a special string in LangGraph/ChapterGraph logic
    assert route_on_eval(state) == "__end__"

def test_route_on_eval_retry():
    state: ChapterState = {"eval_score": 0.5, "iteration": 1}
    assert route_on_eval(state) == "research"

def test_route_on_eval_max_iterations():
    state: ChapterState = {"eval_score": 0.5, "iteration": 3}
    assert route_on_eval(state) == "__end__"
