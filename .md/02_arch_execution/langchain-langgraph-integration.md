# LangChain 과 LangGraph 통합 (LangChain and LangGraph Integration)

## 12.1 역할 분리
- **LangChain**: LLM 호출, 도구(Tool), 리트리버(Retriever) 등 개별 컴포넌트 구현.
- **LangGraph**: 전체 워크플로우 런타임 및 상태(State) 관리.

## 12.2 통합 패턴
```python
# Create a chain for a node
chain = prompt | llm | output_parser

def research_node(state: ChapterState) -> ChapterState:
    result = chain.invoke(state)
    return {**state, "research_notes": result}
```
