from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'C:\Users\Даниил\Desktop\perfume_site\venv\.env')

engine = create_async_engine(
        url=os.getenv("USERS_URL"),
        echo=True,
    )

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)