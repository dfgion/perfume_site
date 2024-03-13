import datetime
from pydantic import BaseModel

class FormData(BaseModel):
    login: str
    password: str

class TokenData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'
    
class TokenScopes(BaseModel):
    scopes: list[str] = []
    
class User(BaseModel):
    id: int
    login: str
    email: str 
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
    id: str
    
    

    