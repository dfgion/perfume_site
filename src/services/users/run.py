from fastapi import FastAPI

from starlette.middleware.sessions import SessionMiddleware
from utils.settings import Config

from api import auth_router

import sys
sys.path.append(r'C:\Users\Даниил\Desktop\perfume_site')

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='Oe_Ef1Y38o1KSWM2R-s-Kg')

app.include_router(auth_router)