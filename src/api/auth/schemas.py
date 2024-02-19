from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    login: str
    email: str | None
    
class UserInDB(User):
    hashed_password: str
    

    