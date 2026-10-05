from pydantic import BaseModel


class HealthResponse(BaseModel):
    """健康检查响应模型。"""
    status: str
    version: str
    llm_provider: str
    