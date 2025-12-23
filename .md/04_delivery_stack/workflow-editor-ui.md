# 워크플로우 에디터 UI (Workflow Editor UI)

## 4.3 Workflow Editor UI 스캐폴드

```tsx
// apps/web/components/chapter/ChapterWorkspace.tsx
"use client";

import { useQuery, useMutation } from "@tanstack/react-query";
import { Button } from "@/components/ui/button";
import { ChapterGraphTimeline } from "./ChapterGraphTimeline";
import { ChapterDraftViewer } from "./ChapterDraftViewer";
import { runChapterGraph } from "@/lib/api-client";

type Props = {
  chapterId: string;
  bookId: string;
};

export function ChapterWorkspace({ chapterId, bookId }: Props) {
  const { data: execution, refetch } = useQuery({
    queryKey: ["chapter-execution", chapterId],
    queryFn: () => fetchChapterExecution(chapterId),
    refetchInterval: 5000,
  });

  const mutation = useMutation({
    mutationFn: () => runChapterGraph({ chapterId, bookId }),
    onSuccess: () => refetch(),
  });

  return (
    <div className="flex h-full">
      <div className="flex-1 border-r">
        <ChapterGraphTimeline execution={execution} />
      </div>
      <div className="flex-1 flex flex-col">
        <div className="p-2 border-b flex justify-between items-center">
          <h2 className="font-semibold">Chapter Draft</h2>
          <Button onClick={() => mutation.mutate()} disabled={mutation.isPending}>
            {mutation.isPending ? "Running..." : "Run Chapter Graph"}
          </Button>
        </div>
        <div className="flex-1 overflow-auto">
          <ChapterDraftViewer execution={execution} />
        </div>
      </div>
    </div>
  );
}
```

- `ChapterGraphTimeline` 컴포넌트는 NodeRun 리스트를 타임라인/단계 진행 바 형태로 렌더링.
- `ChapterDraftViewer`는 마지막 상태의 `draft_text`를 Markdown 렌더링.
