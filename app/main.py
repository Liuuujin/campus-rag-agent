import logging

from fastapi import FastAPI
from app.api.v1 import api_router
from app.core.config import settings

logging.basicConfig(
    level=logging.INFO if settings.DEBUG else logging.WARNING,
    format="%(asctime)s  %(levelname)-8s [%(name)s] %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Campus RAG Agent",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 挂上 v1 的所有路由，统一前缀 /api/v1
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.on_event("startup")
async def on_startup() -> None:
    """服务启动时的钩子：预热资源、打印配置。"""
    logger.info("服务启动：%s v%s", settings.PROJECT_NAME, settings.VERSION)
    logger.info("大模型服务：%s", settings.LLM_PROVIDER)
    