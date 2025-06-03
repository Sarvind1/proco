from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    sku: str
    asin: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    cost: float
    quantity: int = 0
    min_quantity: int = 0
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    quantity: Optional[int] = None
    min_quantity: Optional[int] = None
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class InventoryMovementBase(BaseModel):
    product_id: int
    quantity: int
    movement_type: str
    reference_id: Optional[str] = None
    notes: Optional[str] = None

class InventoryMovementCreate(InventoryMovementBase):
    pass

class InventoryMovementResponse(InventoryMovementBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 