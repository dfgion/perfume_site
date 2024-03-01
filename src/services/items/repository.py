from .models import ManufacturerOrm, PerfumeOrm, TagOrm, Associative_Perfume_Tag_Orm
from .utils.main_repository import SqlAlchemyRepository

class ManufacturerRepository(SqlAlchemyRepository):
    model = ManufacturerOrm
    
class PerfumeRepository(SqlAlchemyRepository):
    model = PerfumeOrm
    
class TagRepository(SqlAlchemyRepository):
    model = TagOrm
    
class AssociativeRepository(SqlAlchemyRepository):
    model = Associative_Perfume_Tag_Orm