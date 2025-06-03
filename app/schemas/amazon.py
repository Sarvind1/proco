from pydantic import BaseModel
from typing import Optional

class AmazonBase(BaseModel):
    asin: str
    title: str
    price: float
    stock: int

class AmazonResponse(AmazonBase):
    id: int

    class Config:
        orm_mode = True 