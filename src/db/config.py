import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
        url=os.getenv("URL"),
        echo=True,
    )

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Model(DeclarativeBase):
    pass
