from .models import ProductOrm
from .utils.main_repository import SqlAlchemyRepository

class ProductRepository(SqlAlchemyRepository):
    model = ProductOrm
    
    