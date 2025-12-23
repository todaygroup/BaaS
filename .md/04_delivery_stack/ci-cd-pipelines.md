# CI/CD 파이프라인 (CI-CD Pipelines)

## 5.1 GitHub Actions 워크플로우
- **CI**: 푸시/PR 시 린트, 테스트(pytest/jest), 빌드 확인.
- **CD**: 메인 브랜치 병합 시 스테이징/프로덕션 환경 자동 배포.

```yaml
jobs:
  test:
    steps:
      - name: Run Tests
        run: |
          cd apps/api && pytest
          cd apps/web && npm test
```
- 컨테이너 빌드 후 Cloud Run 또는 ECS로 배포하는 파이프라인 구축.
