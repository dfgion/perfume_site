from fastapi import FastAPI
from .api import auction_router

app = FastAPI()
app.include_router(auction_router)