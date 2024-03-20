import sys

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from utils.settings import Config

from api import auth_router

load_dotenv(dotenv_path=r'./.env')

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='Oe_Ef1Y38o1KSWM2R-s-Kg')

app.include_router(auth_router)