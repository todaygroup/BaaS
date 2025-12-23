# 페르소나 및 세그먼트 (Personas and Segments)

## 3.1 1차 페르소나: “해님” (전략 컨설턴트·저자)
- **역할**: 전략 컨설턴트, 강연자, 저자.
- **Pain**: 대량의 노트·리포트가 책 구조로 재조합되지 못하고 있음.
- **목표**: 본인의 IP를 책/강의/워크북으로 빠르게 확장.

## 3.2 2차 페르소나
- 전문 강사·인플루언서, 기업 내부 컨설턴트, 출판사 편집자 등.

## 3.3 세그먼트 구분
- 규모: 1인 저자, 스몰 팀, 조직.
- 도메인: 전략/마케팅/기술/교육 등.
- 플랜: 개인(Author) / 팀(Studio) / 엔터프라이즈(Publisher).

```yaml
# personas-and-segments.example.yml
personas:
  - id: "author-hanim"
    role: "Strategic consultant & author"
    pains:
      - "Too many scattered notes and reports."
      - "Not enough time to structure and write a full book."
    goals:
      - "Turn consulting IP into 1–2 books per year."
segments:
  - id: "solo-author"
    description: "Single author with own IP library"
  - id: "team-studio"
    description: "Small content studio / consulting team"
  - id: "enterprise-publisher"
    description: "Publishing / L&D org building multiple titles"
```
