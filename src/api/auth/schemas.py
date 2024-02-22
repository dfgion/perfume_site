import datetime
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    id: int
    username: str
    login: str
    email: str | None
    hashed_password: str
    points: int
    photo_path: str
    create_at: datetime.date
    update_at: datetime.date
    
    class Config:
        from_attributes = True
    
    
class UserInDB(User):
    hashed_password: str
    

    