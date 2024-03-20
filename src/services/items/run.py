from dotenv import load_dotenv
from fastapi import FastAPI

from api import items_router

load_dotenv(dotenv_path='./.env')

app = FastAPI()
app.include_router(items_router)
