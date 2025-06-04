import sys
import os
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal
from app.models.user import User
from app.models.product import Product, InventoryMovement
from app.models.purchase_order import Supplier
from app.core.security import get_password_hash

def seed_data():
    """Seed the database with sample data"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Data already exists, skipping seed...")
            return
        
        print("Seeding database with sample data...")
        
        # Create admin user
        admin_user = User(
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            is_superuser=True
        )
        db.add(admin_user)
        
        # Create regular user
        regular_user = User(
            username="user",
            email="user@example.com",
            hashed_password=get_password_hash("user123"),
            is_active=True,
            is_superuser=False
        )
        db.add(regular_user)
        
        # Create sample suppliers
        suppliers = [
            Supplier(
                name="Tech Supplies Inc",
                contact_name="John Smith",
                email="john@techsupplies.com",
                phone="+1-555-0101",
                address="123 Tech Street, Silicon Valley, CA",
                is_active=True
            ),
            Supplier(
                name="Office Essentials",
                contact_name="Sarah Johnson",
                email="sarah@officeessentials.com",
                phone="+1-555-0102",
                address="456 Office Ave, Business City, NY",
                is_active=True
            ),
            Supplier(
                name="Global Electronics",
                contact_name="Mike Chen",
                email="mike@globalelectronics.com",
                phone="+1-555-0103",
                address="789 Electronics Blvd, Tech Town, TX",
                is_active=True
            )
        ]
        
        for supplier in suppliers:
            db.add(supplier)
        
        # Create sample products
        products = [
            Product(
                sku="LAP-001",
                asin="B08N5WRWNW",
                name="Gaming Laptop",
                description="High-performance gaming laptop with RTX graphics",
                price=1299.99,
                cost=899.99,
                quantity=15,
                min_quantity=5,
                is_active=True
            ),
            Product(
                sku="MON-001",
                asin="B07CVL2D2S",
                name="4K Monitor",
                description="27-inch 4K UHD monitor with USB-C",
                price=399.99,
                cost=299.99,
                quantity=8,
                min_quantity=3,
                is_active=True
            ),
            Product(
                sku="KEY-001",
                asin="B01E8KO2B0",
                name="Mechanical Keyboard",
                description="RGB mechanical gaming keyboard",
                price=129.99,
                cost=79.99,
                quantity=25,
                min_quantity=10,
                is_active=True
            ),
            Product(
                sku="MOU-001",
                asin="B07GBK5V5C",
                name="Wireless Mouse",
                description="Ergonomic wireless gaming mouse",
                price=49.99,
                cost=29.99,
                quantity=30,
                min_quantity=15,
                is_active=True
            ),
            Product(
                sku="HDD-001",
                asin="B07H289S79",
                name="External Hard Drive",
                description="2TB USB 3.0 external hard drive",
                price=79.99,
                cost=59.99,
                quantity=12,
                min_quantity=5,
                is_active=True
            ),
            Product(
                sku="CAM-001",
                asin="B08G8BS2VZ",
                name="Webcam HD",
                description="1080p HD webcam with auto-focus",
                price=89.99,
                cost=65.99,
                quantity=6,
                min_quantity=8,  # This will show as low stock
                is_active=True
            )
        ]
        
        for product in products:
            db.add(product)
        
        # Commit to get product IDs
        db.commit()
        
        # Create sample inventory movements
        movements = [
            InventoryMovement(
                product_id=1,  # Gaming Laptop
                quantity=10,
                movement_type="purchase",
                reference_id="PO-2024-001",
                notes="Initial stock purchase"
            ),
            InventoryMovement(
                product_id=2,  # 4K Monitor
                quantity=12,
                movement_type="purchase",
                reference_id="PO-2024-002",
                notes="Restock for Q1"
            ),
            InventoryMovement(
                product_id=1,  # Gaming Laptop
                quantity=2,
                movement_type="sale",
                reference_id="SO-2024-001",
                notes="Customer order - 2 units"
            ),
            InventoryMovement(
                product_id=3,  # Mechanical Keyboard
                quantity=50,
                movement_type="purchase",
                reference_id="PO-2024-003",
                notes="Bulk purchase for better pricing"
            ),
            InventoryMovement(
                product_id=4,  # Wireless Mouse
                quantity=40,
                movement_type="purchase",
                reference_id="PO-2024-004",
                notes="Popular item restock"
            ),
            InventoryMovement(
                product_id=2,  # 4K Monitor
                quantity=4,
                movement_type="sale",
                reference_id="SO-2024-002",
                notes="Corporate order"
            ),
            InventoryMovement(
                product_id=5,  # External Hard Drive
                quantity=20,
                movement_type="purchase",
                reference_id="PO-2024-005",
                notes="Storage solutions restock"
            ),
            InventoryMovement(
                product_id=3,  # Mechanical Keyboard
                quantity=25,
                movement_type="sale",
                reference_id="SO-2024-003",
                notes="Gaming setup sales"
            ),
            InventoryMovement(
                product_id=4,  # Wireless Mouse
                quantity=10,
                movement_type="sale",
                reference_id="SO-2024-004",
                notes="Accessory bundle sales"
            ),
            InventoryMovement(
                product_id=5,  # External Hard Drive
                quantity=8,
                movement_type="sale",
                reference_id="SO-2024-005",
                notes="Data backup solutions"
            ),
            InventoryMovement(
                product_id=6,  # Webcam HD
                quantity=15,
                movement_type="purchase",
                reference_id="PO-2024-006",
                notes="Work from home demand"
            ),
            InventoryMovement(
                product_id=6,  # Webcam HD
                quantity=9,
                movement_type="sale",
                reference_id="SO-2024-006",
                notes="Remote work setup"
            ),
            InventoryMovement(
                product_id=1,  # Gaming Laptop
                quantity=7,
                movement_type="purchase",
                reference_id="PO-2024-007",
                notes="Restocking best seller"
            )
        ]
        
        for movement in movements:
            db.add(movement)
        
        db.commit()
        print("✅ Database seeded successfully!")
        print("👤 Admin user: admin / admin123")
        print("👤 Regular user: user / user123")
        print("📦 Created 6 sample products")
        print("📈 Created 13 inventory movements")
        print("🏢 Created 3 suppliers")
        
    except Exception as e:
        print(f"❌ Error seeding database: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()