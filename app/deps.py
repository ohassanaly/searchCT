from fastapi import Depends
from chromadb.api import ClientAPI
from chromadb.api.models.Collection import Collection
from openai import OpenAI
from .settings import Settings


class AppState:
    settings: Settings | None = None
    openai_client: OpenAI | None = None
    chroma_client: ClientAPI | None = None
    collection: Collection | None = None


state = AppState()


def get_settings() -> Settings:
    assert state.settings is not None
    return state.settings


def get_openai_client(_: Settings = Depends(get_settings)) -> OpenAI:
    assert state.openai_client is not None
    return state.openai_client


def get_collection(_: Settings = Depends(get_settings)):
    assert state.collection is not None
    return state.collection
