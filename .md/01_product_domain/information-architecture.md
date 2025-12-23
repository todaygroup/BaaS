# 정보 아키텍처 (Information Architecture)

## 5.1 상위 정보 계층
- Workspace → Project → Book → Part/Chapter → GraphRun/Execution → Export

## 5.2 URL 패턴 (Next.js 기준)
```text
/workspaces/:workspaceId/projects/:projectId/books/:bookId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/chapters/:chapterId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/graphs/:graphRunId
/workspaces/:workspaceId/projects/:projectId/books/:bookId/exports
```

```ts
// information-architecture.example.ts
export const routes = {
  bookOverview: (wsId: string, projId: string, bookId: string) =>
    `/workspaces/${wsId}/projects/${projId}/books/${bookId}`,
  chapterWorkspace:
    (wsId: string, projId: string, bookId: string, chapterId: string) =>
      `/workspaces/${wsId}/projects/${projId}/books/${bookId}/chapters/${chapterId}`,
};
```
