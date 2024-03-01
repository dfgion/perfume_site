import datetime

from typing import Optional, List

from sqlalchemy import DATE, Float, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

class Model(DeclarativeBase):
    pass


class ManufacturerOrm(Model):
    __tablename__ = 'manufacturers'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    perfumes: Mapped[List["PerfumeOrm"]] = relationship(backref="manufacturer")
    
    def __repr__(self) -> str:
        return f"<Manufacturer_name: {self.name}>"
    


class PerfumeOrm(Model):
    __tablename__ = "perfumes"
    
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    create_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today())
    photo_path: Mapped[str] = mapped_column(unique=True, nullable=False)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"))
    tags: Mapped[List["TagOrm"]] = relationship(secondary="Associative_Perfume_Tag_Orm", backref='perfume')
    
    def __repr__(self) -> str:
        return f"<Perfume_name: {self.name}>"
    
class TagOrm(Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    perfumes: Mapped[List["PerfumeOrm"]] = relationship(secondary="Associative_Perfume_Tag_Orm", backref='tag')
    
    def __repr__(self) -> str:
        return f"<Tag_name: {self.name}>"
    
class Associative_Perfume_Tag_Orm(Model):
    __tablename__ = "associative_perfume_tag"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    perfume_id: Mapped[int] = mapped_column(ForeignKey("perfumes.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
    __table_args__ = (UniqueConstraint(perfume_id, tag_id, name='index_perfume_tag'),)
    
    