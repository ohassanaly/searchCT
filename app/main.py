from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import chromadb
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .deps import state
from .settings import Settings
from .middleware import log_middleware
from .logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    state.settings = settings

    state.openai_client = (
        OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else OpenAI()
    )
    state.chroma_client = chromadb.CloudClient(
        api_key=settings.chromadb_api_key,
        tenant=settings.chroma_tenant,
        database=settings.chroma_database,
    )
    state.collection = state.chroma_client.get_collection(
        name=settings.chroma_collection
    )
    logger.info("searchCT startup complete")
    try:
        yield
    finally:
        logger.info("searchCT shutting down")


def create_app() -> FastAPI:
    app = FastAPI(title="searchCT", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
    app.include_router(router)
    return app


app = create_app()
