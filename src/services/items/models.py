import datetime
from typing import List

from sqlalchemy import DATE, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Model(DeclarativeBase):
    pass


class Brand(Model):
    __tablename__ = 'brands'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    perfumes: Mapped[List["Perfume"]] = relationship(backref="brand")
    
    def __repr__(self) -> str:
        return f"<Brand_name: {self.name}>"
    


class Perfume(Model):
    __tablename__ = "perfumes"
    
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    create_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today())
    photo_path: Mapped[str] = mapped_column(unique=True, nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    tags: Mapped[List["Tag"]] = relationship(secondary="Associative_Perfume_Tag", backref='perfume')
    
    def __repr__(self) -> str:
        return f"<Perfume_name: {self.name}>"


class Tag(Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    perfumes: Mapped[List["Perfume"]] = relationship(secondary="Associative_Perfume_Tag", backref='tag')
    
    def __repr__(self) -> str:
        return f"<Tag_name: {self.name}>"


class Associative_Perfume_Tag(Model):
    __tablename__ = "associative_perfume_tag"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    perfume_id: Mapped[int] = mapped_column(ForeignKey("perfumes.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
    __table_args__ = (UniqueConstraint(perfume_id, tag_id, name='index_perfume_tag'),)
