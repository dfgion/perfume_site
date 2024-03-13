from abc import ABC, abstractclassmethod
import uuid

from .tools import By
from .exceptions import ByException
from .db_config import async_session
from schemas import User, RegistratedUser
from models import UserOrm

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
    
    async def get_user(self, by: str = By.ID, user_id: int | None = None, login: str | None = None, email: str | None = None) -> User:
        async with async_session() as session:
            if by == By.ID:
                stmt = select(self.model).where(self.model.id == user_id)
            elif by == By.EMAIL:
                stmt = select(self.model).where(self.model.email == email)
            elif by == By.LOGIN:
                stmt = select(self.model).where(self.model.login == login)
            else:
                raise ByException('Unsupported type of by')
            res: UserOrm = (await session.execute(stmt)).first()
            try:
                user = res.to_read_model()
            except:
                print('Unsupported method')
                return None
            return user
        
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
                
            