from datetime import timedelta
import os


class Config:
    DB_URL: str = os.getenv('DB_URL')
    SECRET: str = os.getenv('SECRET')
    ALGORITHM: str = os.getenv('ALGORITHM')
    GOOGLE_CLIENT_ID: str = os.getenv('CLIENT_ID')
    GOOGLE_CLIENT_SECRET: str = os.getenv('CLIENT_SECRET')
    JWT_EXP_ACCESS: timedelta = timedelta(days=1)
    JWT_EXP_REFRESH: timedelta = timedelta(days=3)
    