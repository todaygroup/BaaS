# 상태 관리 & 데이터 패칭 (State & Data Fetching)

## 4.2 데이터 패칭 – RSC + TanStack Query

```ts
// apps/web/app/workspaces/[workspaceId]/projects/[projectId]/books/[bookId]/page.tsx
import { fetchBookDetail } from "@/lib/api-client";
import BookOverview from "@/components/book/BookOverview";

export default async function BookPage({ params }: { params: { workspaceId: string; projectId: string; bookId: string }}) {
  const book = await fetchBookDetail(params.bookId);
  return <BookOverview book={book} />;
}
```

```ts
// apps/web/lib/api-client.ts
export async function fetchBookDetail(bookId: string) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books/${bookId}`, {
    cache: "no-store",
  });
  if (!res.ok) throw new Error("Failed to fetch book");
  return res.json();
}
```

Chapter Workspace는 클라이언트 컴포넌트 + TanStack Query를 사용해 **그래프 실행 상태를 폴링/스트리밍**.
