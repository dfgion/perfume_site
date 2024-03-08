from .repository import UserRepository
from .utils.tools import By

from fastapi import Depends, HTTPException, status

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def check_login(login: str):
    res = await UserRepository.get_user(by = By.LOGIN)
    if res:
        return False
    return True
    
async def check_email(email: str):
    res = await UserRepository.get_user(by = By.EMAIL)
    if res:
        return False
    return True

async def create_user(login: str, email: str, hashed_password: str):
    res = await UserRepository.create_user(login, email, hashed_password)

async def registrate(login: str | None, email: str | None, password: str | None):
    if (await check_login()) == False:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this login is already exists"
                )
    if (await check_email()) == False:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email is already exists"
                )
    hashed_password = get_password_hash(password)
    return await create_user(login=login, email=email, hashed_password=hashed_password)
    