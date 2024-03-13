from datetime import datetime, timedelta
from typing import Annotated

from redis import asyncio as aioredis

from pydantic import ValidationError

from repository import UserRepository
from utils.tools import By
from utils.settings import Config
from schemas import RegistratedUser, TokenScopes, User, TokenData

from jose import JWTError, jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={'refresh': 'permission for refreshing'},
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def check_login(login: str):
    user = await UserRepository.get_user(by = By.LOGIN, login=login)
    if user:
        return False
    return True
    
async def check_email(email: str):
    user = await UserRepository.get_user(by = By.EMAIL, email=email)
    if user:
        return False
    return True

async def authenticate_user(username: str, password: str):
    user: User = await UserRepository.get_user(by=By.LOGIN, login=username)
    if not user:
        return False
    if verify_password(password, user.hashed_password) == False:
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET, algorithm=Config.ALGORITHM)
    return encoded_jwt

async def create_refresh_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET, algorithm=Config.ALGORITHM)
    r = await aioredis.from_url("redis://localhost:8730")
    await r.setex(
        name=data['sub'],
        time=timedelta(days=3),
        value=encoded_jwt
    )
    return encoded_jwt

async def refresh_jwt_token(refresh_token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Bad refresh token"
    )
    try:
        payload = jwt.decode(refresh_token, key=Config.SECRET, algorithms=[Config.ALGORITHM])
        login: str = payload.get("sub")
        if login is None:
            raise credentials_exception
        token_scopes: list = payload.get("scopes", [])
        token_data = TokenScopes(scopes=token_scopes)
    except (JWTError, ValidationError):
        raise credentials_exception
    user: User = await UserRepository.get_user(by=By.LOGIN, login=login)
    if user is None:
        raise credentials_exception
    if 'refresh' not in token_data.scopes:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
            )
    r = await aioredis.from_url("redis://localhost:8730")
    user_refresh_token = await r.get(name=user.login)
    await r.aclose()
    if user_refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The access token expired"
            )
    if user_refresh_token != refresh_token:
        raise credentials_exception
    access_token_expires = Config.JWT_EXP_ACCESS
    access_token = create_access_token(
        data = {
                "sub": user.login, 
                "scopes": ['me'], 
                },
        expires_delta=access_token_expires,
        )
    refresh_token_expires = Config.JWT_EXP_REFRESH
    refresh_token = await create_refresh_token(
        data = {
                "sub": user.login, 
                "scopes": ['refresh'],
                },
        expires_delta=refresh_token_expires
        )
    return TokenData(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type='bearer'
        )

async def create_user(login: str, email: str, hashed_password: str) -> RegistratedUser:
    response: RegistratedUser = await UserRepository.create_user(login, email, hashed_password)
    return response

async def registrate(login: str | None, email: str | None, password: str | None):
    if (await check_login(login=login)) == False:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this login is already exists"
                )
    if (await check_email(email=email)) == False:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email is already exists"
                )
    hashed_password = get_password_hash(password)
    response: RegistratedUser = await create_user(login=login, email=email, hashed_password=hashed_password)
    return response
    