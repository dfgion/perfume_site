from fastapi import FastAPI
from .api import items_router

app = FastAPI()
app.include_router(items_router)