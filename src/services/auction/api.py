from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter

from .schemas import UserProduct, User
from .dependencies import get_active_user


auction_router = APIRouter(prefix='/api/v1', tags='auction')

@auction_router.get(path='/products/me', response_model=list[UserProduct])
async def get_products(current_user = Annotated[User, Depends(get_active_user)]):
    pass


