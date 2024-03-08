import datetime
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        from_attributes = True
    
class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    id: int
    username: str
    email: str | None
    hashed_password: str
    tg_id: str | None
    photo_path: str
    create_at: datetime.date
    update_at: datetime.date
    
    class Config:
        from_attributes = True
        
class RegistrateUser(BaseModel):
    login: str 
    email: str 
    password: str
    
class RegistratedUser(BaseModel):
    id: int
    
    
class UserInDB(User):
    id: str
    

    