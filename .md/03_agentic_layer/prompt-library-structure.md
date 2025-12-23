# 프롬프트 라이브러리 구조 (Prompt Library Structure)

```text
/03_llm_rag_agents/prompts/
  developer/
    global_rules.md
    safety_policies.md
  system/
    book_context.md
    chapter_context.md
  user/
    plan_book.md
    write_chapter.md
    evaluate_chapter.md
  tool/
    rag_result_format.md
    eval_result_format.md
```

각 파일에는 “프롬프트 텍스트 + 사용 예시 + 버전 메타데이터”를 포함.

```yaml
# /03_llm_rag_agents/prompts/metadata.yml
prompts:
  - id: "write_chapter_v1"
    path: "user/write_chapter.md"
    purpose: "Full chapter draft for strategic business books"
    version: "1.0.0"
    created_at: "2025-01-01"
```
