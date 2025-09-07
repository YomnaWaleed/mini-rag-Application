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

app = FastAPI()


@app.get("/welcome")
def welcome():
    return {"message": "Hello world!"}
