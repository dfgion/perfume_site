from abc import ABC, abstractclassmethod

class AbstractRepository(ABC):
    @abstractclassmethod
    async def get_products():
        raise NotImplementedError
    
    @abstractclassmethod
    async def get_user_products():
        raise NotImplementedError
    
class SqlAlchemyRepository(AbstractRepository):
    model = None
    
    async def get_products():
        pass
    
    async def get_user_products():
        pass