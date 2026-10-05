"""应用配置。

所有可变的设置都集中在这里，从环境变量 / .env 文件读取。
用法：from app.core.config import settings
"""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用设置。字段默认值即开发环境默认值。"""

    # ---- 服务 ----
    PROJECT_NAME: str = "Campus RAG Agent"
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # ---- 大模型 ----
    # provider 可选 "ollama"（本地免费）或 "openai"（任何 OpenAI 兼容服务）
    LLM_PROVIDER: str = "ollama"

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:7b"
    OLLAMA_EMBED_MODEL: str = "nomic-embed-text"

    # OpenAI 兼容服务（DeepSeek / 通义 / OpenRouter 等都行）
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.deepseek.com/v1"
    OPENAI_MODEL: str = "deepseek-chat"

    # ---- 生成参数 ----
    TEMPERATURE: float = 0.2   # 问答场景要稳，别太发散
    MAX_LOOPS: int = 3         # Agent 自纠正最多重试几轮

    # Pydantic 会自动读取项目根目录的 .env 文件
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """返回全局唯一的 Settings 实例。

    @lru_cache 保证多次调用只创建一次对象，避免重复读文件。
    """
    return Settings()


settings = get_settings()