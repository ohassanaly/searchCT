from app.query_vector_db import rephrase_query, query, rank_query_result
from app.logger import logger
from pytest import fixture
from openai import OpenAI
from dotenv import load_dotenv
import chromadb
import os
import json

load_dotenv()
client = OpenAI()
chroma_client = chromadb.CloudClient(
    api_key=os.getenv("chromadb_api_key"),
    tenant=os.getenv("chroma_tenant"),
    database="rct_rag",
)
collection = chroma_client.get_collection(name="rct_sections")


@fixture()
def sentence_query():
    return "dose-finding in double-blind cryoglobulinemia vasculitis trial"


@fixture()
def search_result():
    return {
        "ids": [
            ["study A", "study B"],
            ["study C", "study A"],
            ["study D", "study B"],
            ["study E", "study B"],
        ],
        "distances": [[0, 4], [8, 10], [0, 2], [1, 1.5]],
        "documents": [
            ["text A", "text B"],
            ["text C", "text A"],
            ["text D", "text B"],
            ["text E", "text B"],
        ],
    }


def test_rephrase(sentence_query):
    rephrased = rephrase_query(sentence_query, client)
    print(rephrased)
    assert len(rephrased) == 3


def test_query(sentence_query):
    result = query(sentence_query, collection, client, logger)
    assert len(result["ids"]) == len(result["distances"]) == len(result["documents"])


def test_rerank(search_result):
    x = rank_query_result(search_result)
    result = json.loads(x)
    ids = [d["id"] for d in result]
    distances = [d["distance"] for d in result]
    doc_texts = [d["doc_text"] for d in result]
    assert ids == ["study D", "study E", "study B"]
    assert distances == [0, 1, 2.5]
    assert doc_texts == ["text D", "text E", "text B"]
