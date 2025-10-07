from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str

    # Chroma
    chromadb_api_key: str
    chroma_tenant: str
    chroma_database: str = "rct_rag"
    chroma_collection: str = "rct_sections"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
