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
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.include_router(base.base_router)
app.include_router(data.data_router)
