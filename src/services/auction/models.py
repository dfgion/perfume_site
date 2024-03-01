import datetime
from typing import Optional, Annotated

from sqlalchemy import DATE, Float, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .schemas import Product

class Model(DeclarativeBase):
    pass

class ProductOrm(Model):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    perfume_id: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)
    
    def to_read_model(self) -> Product:
        return Product(perfume_id=self.perfume_id,
                     user_id=self.user_id,
                     price=self.price)