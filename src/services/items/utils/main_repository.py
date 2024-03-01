from abc import ABC, abstractclassmethod

class AbstractRepository(ABC):
    @abstractclassmethod
    async def get_user():
        raise NotImplementedError
    
class SqlAlchemyRepository(AbstractRepository):
    model = None
    
    async def get_all():
        pass
    
    async def get_one():
        pass