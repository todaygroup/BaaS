텍스트만으로는 실제 Figma 수준의 hi-fi를 그릴 수는 없지만, 화면 단위·레이아웃·컴포넌트 수준까지 **그대로 디자이너/프론트에 넘길 수 있는 hi-fi 스펙**을 정리해 줄 수 있습니다. 각 화면은 shadcn/ui + Tailwind 기준으로 상정했습니다.

***

## 1. Global Shell (공통 레이아웃)

- 상단 App Bar  
  - 좌측: 로고(텍스트 “BAAS”), 워크스페이스 셀렉터(`<Select>`).  
  - 중앙: 현재 컨텍스트(“Project / Book / Chapter” 브레드크럼).  
  - 우측: 알림 아이콘(Bell), 비용/토큰 요약 Badge, 유저 아바타 메뉴.  

- 좌측 Sidebar  
  - 섹션 헤더: “Main” / “Workspace” / “Settings”.  
  - 항목:
    - Dashboard  
    - Projects  
    - Books  
    - Executions  
    - Prompt Library  
    - Settings  

- 기본 레이아웃 구조 (Tailwind)  
  - `div.flex.h-screen`  
    - `aside.w-64.border-r`  
    - `div.flex.flex-col.flex-1` (상단 헤더 + Content).

***

## 2. Dashboard 화면 (로그인 후 첫 화면)

### 2.1 레이아웃

- 좌측 상단: “최근 실행 / In Progress” 카드  
- 우측 상단: “책 프로젝트” 그리드  
- 하단: “추천 액션 / 템플릿” 영역  

### 2.2 주요 컴포넌트

- In Progress 카드 (shadcn `Card`)  
  - 상단: 실행 타입 Badge (Book / Chapter / Eval).  
  - 본문:
    - 제목: “챕터 3 – 챕터 그래프 실행 중”  
    - Subtext: “예상 소요: ~1–2분 / 마지막 업데이트: 10초 전”  
    - Progress Bar (단계 수 기반 0–100%)  
    - Status Chip: Running / Pending / Failed.  
  - 하단 버튼:
    - “자세히 보기” (Execution Detail 화면 링크)  
    - “중단” (Confirm Dialog)  

- Book 카드 (3열 Grid)  
  - Title, Subtitle, 진행률(완료한 챕터/전체), 상태(Outline / Drafting / Editing).  
  - CTA:
    - “Book Overview 열기”  
    - “새 챕터 생성”  

- “빠른 시작” 영역  
  - 버튼:
    - “새 책 기획”  
    - “기존 리포트 → 책 변환”  
    - “프롬프트 라이브러리 열기”  

***

## 3. Project List / Book List 화면

### 3.1 Project List

- 상단  
  - 제목: “Projects”  
  - 우측: “새 프로젝트 생성” 버튼 (Dialog: 이름/설명/템플릿 선택).  

- 본문  
  - Table 컴포넌트:
    - 컬럼: 이름, 책 수, 최근 업데이트, 상태, 액션(열기/아카이브).  
    - 필터: 상태(Active/Archived), 검색(텍스트).  

### 3.2 Book List (Project Detail)

- 상단  
  - 왼쪽: 프로젝트 정보 카드(이름, 설명, Owner, 총 책 수).  
  - 오른쪽: “새 책 생성” 버튼 → Book Prompt Form 슬라이드오버.

- Book 리스트  
  - Table 또는 Card Grid  
  - Book row:
    - 제목, 독자, 상태, 완료 챕터/전체, 마지막 실행 결과(Icon + 텍스트).  
    - Row 클릭 시 “Book Overview”로 이동.

---

## 4. Book Overview 화면 (책 구조 트리)

### 4.1 레이아웃

- 좌측: Book 메타 정보 패널 (w-1/3)  
- 우측: Part/Chapter 구조 Tree (w-2/3)

### 4.2 좌측 – Book Info Panel

- Card:  
  - Title, Subtitle  
  - Target Audience, Tone, 목표(텍스트).  
  - Stats: 총 챕터 수, 완료 %, 평균 Eval 점수 Badge.  
  - 버튼:
    - “책 메타데이터 편집” (Sheet)  
    - “전체 Book Graph 실행”  

### 4.3 우측 – 구조 트리

- 상단 바  
  - 버튼: “새 Part 추가”, “새 Chapter 추가”, “Outline 재생성”  
  - Toggle: “트리 뷰 / 테이블 뷰”

- 트리 컴포넌트  
  - Part (Accordion or Tree node)  
    - 제목, 설명, 포함 챕터 수  
  - Chapter 리스트:
    - 제목, 상태 Badge(Planned/Researching/Drafted/Revising/Final), Eval Badge  
    - Hover 시 액션 아이콘:
      - “Chapter Workspace 열기”  
      - “Chapter Graph 실행”  
      - “삭제/이동” (드롭다운 메뉴)  

- 정렬/드래그  
  - Drag-and-drop으로 챕터 순서 변경(Handle 아이콘).  
  - 변경 시 오른쪽 상단에 “구조 저장” Toast.

***

## 5. Chapter Workspace 화면 (핵심)

### 5.1 전체 레이아웃

- 상단: 컨텍스트 헤더  
- 본문: 좌측 Graph Timeline / 우측 Draft & Eval  
- 하단: Execution 로그/메타 정보 탭

구조:

```text
Header
└─ Main Area (flex)
   ├─ Left: Graph Timeline (w-1/2)
   └─ Right: Draft & Eval (w-1/2, flex-col)
       ├─ Top: Action Bar
       └─ Middle: Draft Viewer
       └─ Bottom: Eval & Feedback Tabs
```

### 5.2 상단 헤더

- Title: “Chapter 3. 에이전틱 AI 도입 전략”  
- Breadcrumb: Workspace / Project / Book / Chapter  
- 오른쪽:
  - Eval Badge (Eval 0.82)  
  - 상태 Badge (Drafted / Revising)  
  - “챕터 설정” 버튼 (Sheet: 목적/톤/분량 등)

### 5.3 좌측 – Graph Timeline

- Vertical Stepper UI  
  - Step: research → case → write → eval → finalize  
  - 각 Step:
    - Icon (LLM / RAG / Agent symbol)  
    - 상태 Dot: Pending/Running/Done/Failed  
    - 소요 시간, 호출 수 표시  

- Step 클릭 시 상세 패널(오버레이 or Drawer):  
  - 입력/출력 JSON 뷰  
  - 사용 RAG 문서 목록, LLM 호출 로그 요약  

### 5.4 우측 상단 – Action Bar

- 버튼  
  - “챕터 그래프 실행” (Primary; 실제 실행)  
  - “이전 상태로 재실행” (Ghost)  
  - “중단” (Destructive, running 일 때 활성화)  

- Text  
  - “에이전트가 이 챕터 전체를 작성하는 데 30~90초 정도 걸립니다.”  

### 5.5 우측 중단 – Draft Viewer

- 탭: “최신 초안 / 이전 버전 / 비교”  
- Markdown Viewer (react-markdown)  
  - Heading 스타일, 리스트, 강조, 코드 블럭.  
- 상단 오른쪽:  
  - “Export to .md”  
  - “이 내용 편집 모드로 열기” (에디터 화면 연결 or WYSIWYG)  

### 5.6 우측 하단 – Eval & Feedback

- Tabs: “Eval Score / Comments / Change log”  
- Eval Score Tab:  
  - Score Card: Overall / Structure / Logic / Style (바 차트 + 숫자)  
  - “Auto Critic 세부 의견” Accordion  
- Comments Tab:  
  - User Feedback 리스트 (Rating + 텍스트)  
  - “피드백 추가” Textarea + Submit  
- Change log Tab:  
  - 실행 ID별 주요 변경 요약 타임라인

***

## 6. Execution & Debugging 화면

### 6.1 Execution List

- 상단 필터 바  
  - Graph Type(Select) – Book / Chapter / Eval  
  - Status(Filter) – Running / Succeeded / Failed  
  - 기간(DateRangePicker)  
  - 검색(책/챕터 제목, run_id)

- Table  
  - 컬럼: run_id, 타입, 책/챕터, 상태, 시작/종료, 소요시간, Eval 평균  
  - Row 클릭 시 Execution Detail로 이동.

### 6.2 Execution Detail

- 상단: 실행 요약 카드(그래프 타입, 대상, 상태, cost/토큰 합계).  
- 중간: Chapter Workspace와 동일한 Graph Timeline & NodeRun 상세.  
- 하단: Raw 로그(JSON 뷰어) 탭, LLM 호출 리스트 탭.

***

## 7. Prompt Library 화면

### 7.1 구조

- 좌측 Sidebar: 카테고리  
  - Developer / System / User / Tool / Playbooks  
- 우측: 리스트 + 상세

### 7.2 리스트

- 컬럼: 이름, 역할, 목적, 버전, 최근 수정  
- Row 클릭 시 오른쪽 “Prompt Detail” 패널.

### 7.3 Prompt Detail

- 상단: 메타 정보 (역할, 목적, 사용 그래프, 버전 히스토리)  
- 중간: Prompt 본문 (코드 블록 스타일, 편집 가능)  
- 하단: A/B 테스트 결과(성공률·Eval 평균) 미니 차트.

---

## 8. Settings & Integrations 화면

### 8.1 탭 구조

- General  
- Members & Roles  
- Integrations  
- Billing  

### 8.2 Integrations 탭

- Grid 카드: OpenRouter, Supabase, Qdrant/Pinecone, ESP, Slack, Stripe 등  
- 각 카드:
  - 상태 Badge: Connected / Not connected  
  - “연결/설정 변경” 버튼 → OAuth 또는 API Key Form  
  - 마지막 동기화 시간 표시

***

## 9. 모바일/태블릿 대응 (요약)

- 모바일:  
  - Sidebar는 햄버거 메뉴에 숨김.  
  - Dashboard: In Progress → Books 순서로 세로 스크롤.  
  - Chapter Workspace: 상단에 탭으로 “Graph / Draft / Eval” 분리.  

- 태블릿:  
  - 두 열 레이아웃 유지 (Graph Timeline / Draft Viewer)  
  - 세부 패널은 Bottom Sheet 형태 활용.

---

이 스펙을 Figma로 옮길 때는:

- 각 화면을 위 섹션 단위로 Frame 만들고,  
- shadcn 컴포넌트 대응(Buttons, Cards, Tabs, Table, Badge, Sheet, Dialog)을 Tagged 하면서,  
- BAAS 전용 색/타이포 스케일만 정의해 두면 hi-fi wireframe 세트를 빠르게 만들 수 있습니다.