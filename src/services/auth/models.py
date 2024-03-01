import datetime
import uuid

from sqlalchemy import DATE
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from .schemas import User

class Model(DeclarativeBase):
    pass

class UserOrm(Model):
    __tablename__ = 'users'
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(unique=True, nullable=False)
    photo_path: Mapped[str] = mapped_column(unique=True, nullable=True)
    disabled: Mapped[bool] = mapped_column(default=False)
    create_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today())
    update_at: Mapped[datetime.date] = mapped_column(DATE, default=datetime.date.today(), onupdate=datetime.date.today())
    
    def to_read_model(self) -> User:
        return User(id = self.id,
                    username = self.username,
                    login = self.login,
                    email = self.email,
                    hashed_password = self.hashed_password,
                    points = self.points,
                    photo_path = self.photo_path,
                    create_at = self.create_at,
                    update_at = self.update_at
                    )
    