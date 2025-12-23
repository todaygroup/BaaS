# 디버깅 및 데이터 핀닝 (Debugging and Data Pinning)

## 11.1 목적
- 개발 단계에서 동일한 입력 상태로 반복 테스트하기 위해 상태를 파일로 고정(Pin).

## 11.2 구현 예시
```python
import json
from pathlib import Path

PIN_DIR = Path(".pins")

def pin_state(name: str, state: dict):
    PIN_DIR.mkdir(exist_ok=True)
    (PIN_DIR / f"{name}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2))
```
- 특정 시점의 `ChapterState`를 저장하여 로직 수정 후 재현 테스트에 활용.
