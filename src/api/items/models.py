import datetime

from typing import Optional

from sqlalchemy import DATE, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from ...db.config import Model


class PerfumeOrm(Model):
    __tablename__ = "perfumes"
    
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    description: Optional[str] = mapped_column(nullable=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    create_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today())
    
    