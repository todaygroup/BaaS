<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# [관련성 체커(Relevance Checker) 모듈 추가](https://wikidocs.net/267810)  포함하여

그리고 비용적인 부분에 부담으로 인해 open router를 기반으로 구축합니다.
langchain과 langgraph를 혼합하여 구성합니다.
바이브 코딩을 위해 필요한 system, user, assistant, developer, tool 프롬프트는 “메시지의 역할(role)” 기준으로 나뉘는 5가지 프롬프트 구분에 대한 내용도 요구됩니다.

질문에 추가된 세 가지 축을 반영해서, 기존 설계에 **무엇을 어떻게 더해야 완전해지는지**만 딱 짚어 정리하겠습니다.[^1][^2][^3]

***

## 1. Relevance Checker 모듈 편입: 어디에 넣을 것인가

관련성 체커(Relevance Checker)는 **RAG + LangGraph 워크플로우의 “검색 결과 검증 루프”**입니다.[^1]

### 편입 위치

- 디렉터리 3의 **`04-data-rag-infra.md`**와 **`06-service-workflows-and-langgraph.md`**에 다음 챕터를 추가합니다.

1) `04-data-rag-infra.md`에 추가

- “4.x 관련성 체커(Relevance Checker) 모듈”
    - 역할:
        - `question, context`를 입력받아 “이 context가 질문에 실제로 관련 있는가?”를 yes/no 또는 score로 평가.[^1]
    - 구현 패턴:
        - LangChain Runnable/Chain으로 `question_answer_relevant` 정의
        - 프롬프트 예시(groundedness / relevance 체크용 템플릿)
    - 설정 항목:
        - 기준 임계값(threshold), 재검색 회수 제한, 로그/모니터링(얼마나 자주 no가 나오는지).[^1]

2) `06-service-workflows-and-langgraph.md`에 추가

- “3.x Relevance Check 라우팅 패턴”
    - retrieve → relevance_check → (yes → llm_answer, no → retrieve) 구조를 LangGraph 예제로 포함.[^1]
    - `GraphState`에 `question, context, relevance` 필드 정의, `is_relevant` 라우터 함수와 재귀 한도(recursion_limit) 설정을 예시로 명시.[^4][^1]
    - GraphRecursionError 방지 전략(재시도 횟수, fallback 응답 정책)까지 포함.

***

## 2. OpenRouter + LangChain + LangGraph 혼합: 아키텍처·가이드 반영

### 2-1. OpenRouter 기반 LLM 인프라

다음 문서에 OpenRouter 전용 챕터를 추가합니다.

1) `05-llm-and-prompt-engineering.md`

- “2.x LLM Provider 전략 – OpenRouter 중심”
    - OpenRouter를 기본 LLM 게이트웨이로 두고, 모델 선택을 config 기반으로 하는 구조.[^2]
    - 장점: 다수 모델 / 비용 최적화 / 지역 제약 우회.
    - 구현 가이드:
        - LangChain에서 OpenRouter Chat 모델 래퍼 사용
        - 모델 이름·max_tokens·temperature를 환경변수로 주입.

2) `monorepo-structure-and-env.md`

- OpenRouter 관련 환경변수: `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL`, 모델 기본값.
- 환경별(Dev/Stage/Prod) 다른 모델/가격대 구성.


### 2-2. LangChain + LangGraph 혼합 패턴

아키텍처 상에서 제1원칙은 **“LangChain은 빌딩블록, LangGraph는 오케스트레이션 런타임”**입니다.[^5][^2]

1) `03-multi-agent-architecture.md`

- “3.x LangChain 컴포넌트 재사용 전략”
    - Retriever, PromptTemplate, Tool, Chains는 LangChain으로 정의.
    - 이들을 LangGraph의 Node 함수 안에서 호출하는 패턴 정리.[^2][^5]
    - 예:
        - `pdf_retriever = …` (LangChain)
        - `def retrieve(state: GraphState): retriever.invoke(state["question"])` (LangGraph node).[^5][^1]

2) `06-service-workflows-and-langgraph.md`

- “4.x LangChain → LangGraph 마이그레이션 체크리스트”[^2]
    - 1단계: LangChain으로 체인/RAG/프롬프트 검증
    - 2단계: 검증된 컴포넌트를 LangGraph 노드로 감싸 그래프로 조립
    - 3단계: 상태/체크포인트/에러 핸들링 추가.

***

## 3. 5가지 role(system / user / assistant / developer / tool) 프롬프트 가이드 추가

바이브 코딩을 안정적으로 쓰려면, **메시지 role별 책임을 정교하게 분리**해야 합니다.[^6][^7][^3]

### 3-1. 전용 가이드북 챕터

`05-llm-and-prompt-engineering.md`에 아래 챕터 추가:

- “3. 메시지 역할(role)별 프롬프트 설계”


#### (1) developer (구 system) 역할

- 목적: 모델의 **장기적 행동 규칙, 스타일, 금칙사항, 도메인 정책** 정의.[^7][^8][^3]
- 특징:
    - 가장 높은 우선순위, 잘 변하지 않는 “헌법/규칙서”에 가까운 내용.
- 예:
    - “너는 글로벌 워크플로우 빌더 SaaS의 아키텍트 어시스턴트이다. 항상 보안·비용·거버넌스를 고려해 답한다.”
    - “프롬프트 예시는 JSON 코드블록으로만 답하고, 한국어 설명을 함께 제공한다.”


#### (2) system 역할

- 목적: **런타임 컨텍스트·툴 응답·상태 요약** 제공.[^7]
- 예:
    - 이전 대화 요약, 현재 워크플로우 상태, 관련성 체크 결과(예: “현재 검색 결과는 질문과의 관련성이 낮음”)를 system 메시지로 공급.
    - Tool 호출 결과를 system으로 제공해 모델이 “이건 도구가 준 정보”임을 알게 하는 패턴.[^7]


#### (3) user 역할

- 목적: 인간 사용자의 **의도·요구사항·질문·명령** 전달.[^9][^6]
- 바이브 코딩용 user 패턴:
    - “이런 기능을 가진 글로벌 서비스 화면을 설계해줘”,
    - “아래 요구사항을 만족하는 LangGraph 그래프 정의 코드를 생성해줘” 등.


#### (4) assistant 역할

- 목적: LLM **응답을 표현**하는 채널; 모델이 만든 코드·설계·설명을 여기에 기록.[^6][^9]
- 전략:
    - assistant 응답 중 일부를 다시 system 또는 developer로 승격시켜 “새로운 규칙/패턴”으로 재사용하는 메커니즘도 포함(예: 프롬프트 라이브러리 업데이트).[^4]


#### (5) tool 역할

- 목적: **외부 도구 호출·결과**를 표현하는 전용 역할.[^6]
- 예:
    - LangChain의 Tools, LangGraph ToolNode, n8n HTTP Request 결과 등을 tool 메시지로 싱크.
    - 모델이 “지금은 내 추론이 아니라 도구 결과를 읽는 단계”임을 명확히 알도록 설계.


### 3-2. 역할별 템플릿·모듈화

동일 문서에 다음 섹션을 추가:

- “3.x 역할별 프롬프트 템플릿 모듈”
    - `/prompts/developer/*.md`: 제품 전역 규칙, 보안/거버넌스, 톤/스타일.
    - `/prompts/system/*.md`: 각 워크플로우/에이전트별 상태·컨텍스트 요약 템플릿.
    - `/prompts/user/*.md`: 기획/설계/코드 생성/리팩토링/테스트용 바이브 코딩 유저 프롬프트 템플릿.
    - `/prompts/tool/*.md`: 도구 응답 포맷, LLM이 해석하기 쉬운 JSON 스키마.[^3][^10]

***

## 4. 전체 설계에 대한 “누락 여부” 점검 요약

질문에서 추가하신 요구까지 반영하면, 다음이 모두 커버됩니다.

- Relevance Checker 모듈: RAG/워크플로우/에이전트 레벨에서의 관련성·Groundedness 검증 + 재검색 루프.[^1]
- OpenRouter 기반 LLM 인프라: 비용·모델 선택 전략, LangChain 래퍼, 환경변수 설계.[^2]
- LangChain + LangGraph 혼합 구조: LangChain=컴포넌트, LangGraph=그래프 및 상태·에러 런타임.[^5][^2]
- 5 role 프롬프트 체계: developer/system/user/assistant/tool 각각의 책임·예시·템플릿 구조.[^3][^7]

이 추가 챕터들을 각 가이드북에 삽입하면, **바이브 코딩으로 글로벌 서비스를 설계·생성·운영하는데 필요한 구조적 요소는 빠진 것이 없다고 봐도 될 수준**까지 올라갑니다.
<span style="display:none">[^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21]</span>

<div align="center">⁂</div>

[^1]: https://wikidocs.net/267810

[^2]: https://peliqan.io/blog/langchain-vs-langgraph/

[^3]: https://danbibibi.tistory.com/321

[^4]: https://www.swarnendu.de/blog/langgraph-best-practices/

[^5]: https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/

[^6]: https://www.youtube.com/watch?v=xbpdMkTz8L4

[^7]: https://www.reddit.com/r/OpenAIDev/comments/1kotbif/in_the_chat_completions_api_when_should_you_use/

[^8]: https://glasslego.tistory.com/52

[^9]: https://community.openai.com/t/prompts-for-system-assistant-roles/85605

[^10]: https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md

[^11]: https://wikidocs.net/186245

[^12]: https://wikidocs.net

[^13]: https://www.egovframe.go.kr/wiki/doku.php?id=egovframework%3Acompa

[^14]: https://www.kieuns.com/doku.php?id=wiki%3Aplugin-syntax

[^15]: https://github.com/ychoi-kr/wikidocs-chobo-python/actions

[^16]: https://www.kieuns.com/wiki:plugin-syntax

[^17]: https://blog.langchain.com/building-langgraph/

[^18]: https://wikidocs.com

[^19]: https://atomic.snu.ac.kr/api.php?action=help\&recursivesubmodules=1

[^20]: https://www.langchain.com/langgraph

[^21]: http://wiki1.kr/api.php?action=help\&recursivesubmodules=1

