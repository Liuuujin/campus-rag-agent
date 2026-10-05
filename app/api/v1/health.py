from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """返回服务状态。

    别小看这个接口：生产环境里负载均衡、Kubernetes 的存活探针
    都靠它判断服务是否还活着。
    """
    return HealthResponse(
        status="ok",
        version=settings.VERSION,
        llm_provider=settings.LLM_PROVIDER,
    )