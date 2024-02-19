import datetime
from typing import Optional

from pydantic import BaseModel

class Perfume(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    amount: float
    create_at: datetime.date
    