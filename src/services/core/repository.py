from abc import ABC, abstractclassmethod


class AbstractRepository(ABC):
    @abstractclassmethod
    async def create():
        raise NotImplementedError
    
    @abstractclassmethod
    async def read():
        raise NotImplementedError
    
    @abstractclassmethod
    async def update():
        raise NotImplementedError
    
    @abstractclassmethod
    async def delete():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @classmethod
    async def new(cls, settings):
        self = cls()
        self.settings = settings
        self.pool = await create_pool(dsn)
        return self
    
    async def get_all(self):
        raise NotImplementedError
    
    async def get_one(self):
        raise NotImplementedError