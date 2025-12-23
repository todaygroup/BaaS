# 프롬프트 템플릿 & 패턴 (Prompt Templates & Patterns)

## 5.1 챕터 작성 프롬프트 패턴

```python
def build_chapter_writer_messages(
    book_meta: dict,
    chapter_meta: dict,
    outline: dict,
    research_notes: list[dict],
    rag_citations: list[str],
) -> list[dict]:
    system_msg = {
        "role": "system",
        "content": build_system_context(book_meta, chapter_meta, rag_summary="\n\n".join(
            n["text"] for n in research_notes
        )),
    }
    user_msg = {
        "role": "user",
        "content": f"""
아래 정보를 바탕으로 이 챕터의 초안을 작성해줘.

[요구사항]
- 제목과 소제목을 명확히 구조화할 것
- 사례와 인사이트를 적절히 섞되, 과장하지 말 것
- 마케팅 문구가 아니라, 전략 컨설팅 리포트 스타일에 가깝게

[출력 형식]
- Markdown
- H2: 챕터 제목 (이미 정해져 있으면 재사용)
- H3: 주요 섹션 제목
- 필요한 경우 Bullet/Numbered list 사용

[Outline JSON]
{outline}

[RAG 문맥 출처 ID]
{rag_citations}
""",
    }
    return [
        {"role": "system", "content": DEVELOPER_PROMPT},
        system_msg,
        user_msg,
    ]
```

이 패턴을 Planner/Research/CaseStudy/AutoCritic 등에 각각 정의한다.
