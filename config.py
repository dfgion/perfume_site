from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r'C:\Users\Даниил\Desktop\perfume_site\venv\.env')

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
USERS_URL = os.environ.get('USERS_URL')
