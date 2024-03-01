from typing import Annotated

from fastapi import FastAPI, Depends

from .schemas import UserProduct, User
from .dependencies import get_active_user

auction = FastAPI()




@auction.get(path='products/me', response_model=list[UserProduct])
async def get_products(current_user = Annotated[User, Depends(get_active_user)]):
    pass


