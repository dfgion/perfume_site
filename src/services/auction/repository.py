from .models import ProductOrm
from .utils.main_repository import SqlAlchemyRepository

class AuctionRepository(SqlAlchemyRepository):
    model = ProductOrm
    
    