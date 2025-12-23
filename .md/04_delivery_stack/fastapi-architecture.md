# FastAPI 아키텍처 (FastAPI Architecture)

## 3.1 프로젝트 구조
- `app/main.py`: 엔트리포인트 및 미들웨어 설정.
- `app/routes/`: 리소스별 라우터 분리 (`books.py`, `chapters.py`, `graphs.py`).
- `app/deps.py`: 의존성 주입 (Settings, Graphs, DB).

## 3.2 핵심 설정
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = "dev"
    openrouter_api_key: str
    database_url: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```
- FastAPI의 `Depends`를 활용하여 서비스 레이어와 저장소 레이어를 주입함.
