from pydantic_settings import BaseSettings, SettingsConfigDict

class WorkerSettings(BaseSettings):
    env: str = "development"
    
    # Infrastructure
    db_url: str = "postgresql://dev:dev@localhost:5432/baas"
    vector_db_url: str = "http://localhost:6333"
    vector_db_key: str = ""
    
    # Worker Logic
    job_type: str = "rag_ingest"

    model_config = SettingsConfigDict(
        env_file=(".env.development", "apps/worker/.env.development.local"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

worker_settings = WorkerSettings()
