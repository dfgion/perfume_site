from abc import ABC, abstractclassmethod
from typing import Any, Awaitable, Callable
import uuid

from .tools import By
from .exceptions import ByException
from .db_config import async_session
from ..schemas import User, RegistratedUser

from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError
    
class AbstractRepository(ABC):
    @abstractclassmethod
    async def get_user():
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_user():
        raise NotImplementedError
    
class SqlAlchemyRepository(AbstractRepository):
    model = None
    
    async def get_user(self, by: str = By.ID, id: int | None = None, login: str | None = None, email: str | None = None) -> list[User]:
        async with async_session() as session:
            if by == By.ID:
                stmt = select(self.model).where(self.model.id == by)
            elif by == By.EMAIL:
                stmt = select(self.model).where(self.model.email == by)
            elif by == By.LOGIN:
                stmt = select(self.model).where(self.model.login == by)
            else:
                raise ByException('Unsupported type of by')
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
        
    async def create_user(self, login: str, email: str, hashed_password: str) -> RegistratedUser:
        async with async_session() as session:
            try:
                stmt = insert(self.model).values(id=uuid.uuid4(), login=login, email=email, hashed_password=hashed_password).returning(self.model.id)
                res = await session.execute(stmt)
                await session.commit()
            except IntegrityError:
                stmt = insert(self.model).values(id=uuid.uuid4(), login=login, email=email, hashed_password=hashed_password).returning(self.model.id)
                res = await session.execute(stmt)
                await session.commit()
            return res.scalar_one()
                
            