import datetime

from typing import Optional

from sqlalchemy import DATE, Float, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ...db.config import Model

class UserOrm(Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=True)
    login: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(unique=True, nullable=False)
    points: Mapped[int] = mapped_column(unique=False, nullable=False, default=0)
    photo_path: Mapped[str] = mapped_column(unique=True, nullable=True)
    create_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today())
    update_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today(), onupdate=datetime.date.today())
    