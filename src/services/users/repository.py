from models import UserOrm
from utils.main_repository import SqlAlchemyRepository

class UserRepository(SqlAlchemyRepository):
    model = UserOrm