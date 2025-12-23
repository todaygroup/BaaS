from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = "dev"
    openrouter_api_key: str = ""
    database_url: str = "sqlite:///baas.db"
    supabase_url: str = ""
    supabase_key: str = ""
    vector_db_url: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
