import sys
import os
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import Base, engine
from app.models.user import User
from app.models.product import Product, InventoryMovement
from app.models.purchase_order import PurchaseOrder, PurchaseOrderItem, Supplier

def init_db():
    """Initialize the database with all tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 