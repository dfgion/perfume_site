from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI


from test3 import router
# Initialize our OAuth instance from the client ID and client secret specified in our .env file



app = FastAPI()

app.include_router(router)
app.add_middleware(SessionMiddleware, secret_key='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')
