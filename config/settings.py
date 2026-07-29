import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "Climate Guardian AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # LLM & Model Configurations
    MODEL_PROVIDER: str = os.getenv("MODEL_PROVIDER", "openai")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4o")
    TEMPERATURE: float = 0.2
    
    # Vector Database
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    
    # Security Guards
    MAX_INPUT_TOKENS: int = 4096
    ENABLE_PROMPT_GUARD: bool = True

settings = Settings()
