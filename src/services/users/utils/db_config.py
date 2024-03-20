import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from settings import Config

engine = create_async_engine(
        url=Config.USERS_DB_URL,
        echo=True,
    )

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)