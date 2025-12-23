# 외부 통합 (External Integrations)

## 3.5 주요 연동 서비스
- **ESP (Email Service Provider)**: 책 완성 시 원고 다운로드 링크 자동 발송.
- **Slack/Discord**: 에이전트 작업 실패 또는 비용 임계치 초과 시 알림.
- **Stripe**: 유료 서비스 전환 시 구독 및 결제 연동.

```python
def notify_author(email: str, book_title: str, url: str):
    # Send email payload with download link
    pass
```
