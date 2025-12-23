# AI 평가 & 피드백 루프 (AI Evaluation & Feedback Loops)

## 6.1 AgentEval 결과 UX

- Chapter Workspace에 `eval_score`와 `eval_feedback`을 시각적으로 보여주고, “재생성/수정 필요” 여부를 강조.

```tsx
// /05_ux_interaction_ops/components/chapter/ChapterEvalBadge.tsx
export function ChapterEvalBadge({ score }: { score: number | null }) {
  if (score == null) return <span className="text-xs text-muted-foreground">미평가</span>;
  const color =
    score >= 0.8 ? "bg-emerald-100 text-emerald-800" :
    score >= 0.6 ? "bg-amber-100 text-amber-800" :
    "bg-red-100 text-red-800";
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${color}`}>
      Eval {score.toFixed(2)}
    </span>
  );
}
```
