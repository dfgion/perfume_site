from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str | None
    hashed_password: str
    tg_id: str | None
    photo_path: str
    disabled: bool
    create_at: datetime.date
    update_at: datetime.date
    
    class Config:
        from_attributes = True
    
class UserProduct(BaseModel):
    user_id: int
    perfume_name: str
    manufacturer_name: str
    perfume_photo_path: str
    price: float = Field(ge=1)
    
class Product(BaseModel):
    perfume_id: int
    user_id: int
    price: float
    
class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []
    