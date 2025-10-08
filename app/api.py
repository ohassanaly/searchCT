from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .deps import get_collection, get_openai_client
import json

router = APIRouter()


class SearchRequest(BaseModel):
    user_input: str
    criteria: list[str] | None = None


@router.get("/", tags=["meta"])
def welcome_page():
    return {"message": "Welcome to the searchCT API"}


@router.post("/search/", tags=["search"])
async def search_engine(
    payload: SearchRequest,
    collection=Depends(get_collection),
    llm_client=Depends(get_openai_client),
):
    from .logger import logger
    from .query_vector_db import query, rank_query_result

    result = query(
        payload.user_input,
        collection,
        llm_client,
        logger,
        payload.criteria or [],
    )
    return json.loads(rank_query_result(result))
