from fastapi.routing import APIRouter

from repository import PerfumeRepository

items_router = APIRouter(prefix='/api/v1', tags='items')
repo = PerfumeRepository.new()


@items_router.get("/items")
def read_all_items():
    return repo.get_all()


@items_router.post("/items")
def create_item():
    return repo.create()


@items_router.get("/items/{item_id}")
def read_item(item_id: int):
    return repo.get_one()


@items_router.patch("/items/{item_id}")
def read_item(item_id: int):
    return repo.update()


@items_router.delete("/items/{item_id}")
def read_item(item_id: int):
    return repo.delete()