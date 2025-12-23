# 프롬프트 UX 패턴 (Prompt UX Patterns)

## 4.2 입력 패턴
- **Structured Form**: 체계적인 책 기획을 위한 폼 입력.
- **Free-form Vibe**: 저자의 감각적인 지시사항을 받는 텍스트 영역.
- **Context Pinning**: RAG 검색 결과 중 중요한 사례를 고정(Pin)하여 생성에 강제 반영.

```tsx
export function PromptInput() {
  return (
    <div>
      <Textarea placeholder="여기에 저자의 관점이나 사례를 자유롭게 적어주세요..." />
      <div className="flex gap-2">
        <Badge>Professional</Badge>
        <Badge>Friendly</Badge>
      </div>
    </div>
  )
}
```
