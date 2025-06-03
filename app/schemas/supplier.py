from pydantic import BaseModel
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

class SupplierResponse(SupplierBase):
    id: int

    class Config:
        orm_mode = True 