from fastapi import FastAPI, APIRouter
import os
from helpers.config import get_settings

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])


@base_router.get("/")
async def welcome():
    app_name = get_settings().APP_NAME
    app_version = get_settings().APP_VERSION

    return {"app_name": app_name, "app_version": app_version}
