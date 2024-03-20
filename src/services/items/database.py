from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os

engine = create_async_engine(
    # url=os.getenv("ITEMS_DB_URL"),
    url = "postgresql://postgres:postgres@localhost:5432/postgres",
    echo = True,
)

# url = "postgresql://postgres:postgres@localhost:5432/postgres"
# async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session = AsyncSession(engine)
session.connection().execute("SELECT * from actors")