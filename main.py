import uvicorn

from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI()

async def lifespan(app: FastAPI):
    yield
    

