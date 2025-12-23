from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    env: str = "development"

    # Infrastructure
    db_url: str = "postgresql://dev:dev@localhost:5432/baas"
    supabase_url: str = "http://localhost:54321"
    supabase_key: str = "local-dev-key"

    # LLM / RAG
    openrouter_api_key: str = ""
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    vector_db_url: str = "http://localhost:6333"
    vector_db_key: str = ""

    # Observability
    otlp_endpoint: Optional[str] = None

    # App Config
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    model_config = SettingsConfigDict(
        env_file=(".env.development", "apps/api/.env.development.local"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
