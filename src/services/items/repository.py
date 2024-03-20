from .models import Brand, Perfume, Tag, Associative_Perfume_Tag
from ..core.repository import SqlAlchemyRepository


class ManufacturerRepository(SqlAlchemyRepository):
    model = Brand


class PerfumeRepository(SqlAlchemyRepository):
    model = Perfume


class TagRepository(SqlAlchemyRepository):
    model = Tag


class AssociativeRepository(SqlAlchemyRepository):
    model = Associative_Perfume_Tag
