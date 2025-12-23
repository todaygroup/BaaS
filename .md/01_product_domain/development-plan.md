# 개발 계획 (Development Plan)

## 8.1 수직 슬라이스(Vertical Slice) 전략
- **Slice 1**: 단일 챕터 BAAS (연구-집필-평가 루프 완성).
- **Slice 2**: 책 전체 아웃라인 및 초기 챕터 생성.
- **Slice 3**: 전 권 집필 및 최종 Export.

```yaml
milestones:
  - id: "slice1_single_chapter"
    scope:
      - "Single Book"
      - "Single Chapter BAAS flow"
    includes:
      - "ChapterState schema"
      - "chapter_graph v0.1"
```
