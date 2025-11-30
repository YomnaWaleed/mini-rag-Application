"""
from google.colab import userdata
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = userdata["OPENROUTER_API_KEY"]

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

os.environ["OPENAI_API_NAME"] = "openai/gpt-oss-20b:free"
llm = ChatOpenAI(model_name="openai/gpt-oss-20b:free", temperature=0)
print(llm("what is the capital of France?"))
"""

from fastapi import FastAPI
from routes import base, data, nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactor import VectoreDBProviderFactor
from stores.llm.templates.template_parser import TemplateParser

app = FastAPI()


async def startup_span():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

    llm_provider_factory = LLMProviderFactory(settings)
    vectordb_provider_factory = VectoreDBProviderFactor(settings)

    # generation client
    app.generation_client = llm_provider_factory.create(
        provider=settings.GENERATION_BACKEND
    )
    app.generation_client.set_generation_model(model_id=settings.GENERATION_MODEL_ID)

    # embedding client
    app.embedding_client = llm_provider_factory.create(
        provider=settings.EMBEDDING_BACKEND
    )
    app.embedding_client.set_embedding_model(
        model_id=settings.EMBEDDING_MODEL_ID,
        embedding_size=settings.EMBEDDING_MODEL_SIZE,
    )

    # vector db client
    app.vectordb_client = vectordb_provider_factory.create(
        provider=settings.VECTOR_DB_BACKEND
    )
    app.vectordb_client.connect()

    app.template_parser = TemplateParser(
        language=settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,
    )


async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.disconnect()


app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
