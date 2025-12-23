# Prompt-to-Graph 전략 (Prompt-to-Graph Strategy)

## 13.1 목적

- “설명(Describe) → 그래프 설계(Plan) → 그래프 코드(Scaffold)”로 가는 **PTG(프롬프트→그래프)** 자동화.

## 13.2 품질 체크리스트

- 루프/종료 조건 명시 여부.
- 에러 경로/예외 처리 노드 존재 여부.
- 자격 증명/보안 관련 노드 존재 여부.
- 비용 관점에서 불필요한 LLM 호출 루프 여부.

## 13.3 PTG용 프롬프트 예시

```text
[developer]
너는 LangGraph 기반 멀티에이전트 시스템 아키텍트이다.
입력 요구사항을 StateGraph와 노드/에지 정의로 설계한다.

[user]
다음 요구사항을 만족하는 "Chapter Graph"를 설계하고,
Python LangGraph 코드 스캐폴드를 생성해줘.

요구사항:
- State: ChapterState(TypedDict)
- Nodes: research, write, eval
- Flow: research -> write -> eval -> (score<0.8 && iter<3 -> research else END)
- Observability: run_id, node_id 기준 로그 출력
```
