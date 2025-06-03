from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    asin = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    cost = Column(Float)
    quantity = Column(Integer, default=0)
    min_quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    inventory_movements = relationship("InventoryMovement", back_populates="product")
    purchase_orders = relationship("PurchaseOrderItem", back_populates="product")

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    movement_type = Column(String)  # "purchase", "sale", "adjustment", "return"
    reference_id = Column(String)  # PO number, SO number, etc.
    notes = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    product = relationship("Product", back_populates="inventory_movements") 