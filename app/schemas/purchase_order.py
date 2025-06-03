from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class PurchaseOrderStatus(str, Enum):
    DRAFT = "draft"
    PENDING = "pending"
    APPROVED = "approved"
    ORDERED = "ordered"
    RECEIVED = "received"
    CANCELLED = "cancelled"

class PurchaseOrderItemBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

class PurchaseOrderItemCreate(PurchaseOrderItemBase):
    pass

class PurchaseOrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None
    received_quantity: Optional[int] = None

class PurchaseOrderItemResponse(PurchaseOrderItemBase):
    id: int
    purchase_order_id: int
    received_quantity: int = 0
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PurchaseOrderBase(BaseModel):
    po_number: str
    supplier_id: int
    status: PurchaseOrderStatus = PurchaseOrderStatus.DRAFT
    total_amount: float
    currency: str = "USD"
    expected_delivery_date: Optional[datetime] = None
    notes: Optional[str] = None

class PurchaseOrderCreate(PurchaseOrderBase):
    items: List[PurchaseOrderItemCreate]

class PurchaseOrderUpdate(BaseModel):
    status: Optional[PurchaseOrderStatus] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None
    notes: Optional[str] = None

class PurchaseOrderResponse(PurchaseOrderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[PurchaseOrderItemResponse]

    class Config:
        from_attributes = True

class SupplierBase(BaseModel):
    name: str
    contact_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: bool = True

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    contact_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None

class SupplierResponse(SupplierBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 