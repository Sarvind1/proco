import pandas as pd
from typing import List, Dict, Any
import logging
from datetime import datetime
from sqlalchemy.orm import Session

from app.models.product import Product, InventoryMovement
from app.models.purchase_order import PurchaseOrder, PurchaseOrderItem, Supplier

logger = logging.getLogger(__name__)

class CSVImporter:
    def __init__(self, db: Session):
        self.db = db

    def import_products(self, file_path: str) -> List[Dict[str, Any]]:
        """Import products from CSV file"""
        try:
            df = pd.read_csv(file_path)
            results = []
            
            for _, row in df.iterrows():
                try:
                    product = Product(
                        sku=row['sku'],
                        asin=row.get('asin'),
                        name=row['name'],
                        description=row.get('description', ''),
                        price=float(row['price']),
                        cost=float(row.get('cost', 0)),
                        quantity=int(row.get('quantity', 0)),
                        min_quantity=int(row.get('min_quantity', 0))
                    )
                    self.db.add(product)
                    results.append({"sku": product.sku, "status": "success"})
                except Exception as e:
                    results.append({"sku": row.get('sku', 'unknown'), "status": "error", "message": str(e)})
            
            self.db.commit()
            return results
        except Exception as e:
            logger.error(f"Error importing products: {str(e)}")
            raise

    def import_inventory(self, file_path: str) -> List[Dict[str, Any]]:
        """Import inventory movements from CSV file"""
        try:
            df = pd.read_csv(file_path)
            results = []
            
            for _, row in df.iterrows():
                try:
                    product = self.db.query(Product).filter(Product.sku == row['sku']).first()
                    if not product:
                        results.append({"sku": row['sku'], "status": "error", "message": "Product not found"})
                        continue

                    movement = InventoryMovement(
                        product_id=product.id,
                        quantity=int(row['quantity']),
                        movement_type=row['movement_type'],
                        reference_id=row.get('reference_id'),
                        notes=row.get('notes', '')
                    )
                    self.db.add(movement)
                    
                    # Update product quantity
                    product.quantity += int(row['quantity'])
                    
                    results.append({"sku": product.sku, "status": "success"})
                except Exception as e:
                    results.append({"sku": row.get('sku', 'unknown'), "status": "error", "message": str(e)})
            
            self.db.commit()
            return results
        except Exception as e:
            logger.error(f"Error importing inventory: {str(e)}")
            raise

    def import_purchase_orders(self, file_path: str) -> List[Dict[str, Any]]:
        """Import purchase orders from CSV file"""
        try:
            df = pd.read_csv(file_path)
            results = []
            
            for _, row in df.iterrows():
                try:
                    # Get or create supplier
                    supplier = self.db.query(Supplier).filter(Supplier.name == row['supplier_name']).first()
                    if not supplier:
                        supplier = Supplier(
                            name=row['supplier_name'],
                            contact_name=row.get('contact_name'),
                            email=row.get('email'),
                            phone=row.get('phone'),
                            address=row.get('address')
                        )
                        self.db.add(supplier)
                        self.db.flush()

                    # Create purchase order
                    po = PurchaseOrder(
                        po_number=row['po_number'],
                        supplier_id=supplier.id,
                        status=row.get('status', 'draft'),
                        total_amount=float(row['total_amount']),
                        currency=row.get('currency', 'USD'),
                        expected_delivery_date=datetime.strptime(row['expected_delivery_date'], '%Y-%m-%d') if 'expected_delivery_date' in row else None,
                        notes=row.get('notes', '')
                    )
                    self.db.add(po)
                    self.db.flush()

                    # Add items
                    items_df = pd.read_csv(row['items_file']) if 'items_file' in row else None
                    if items_df is not None:
                        for _, item_row in items_df.iterrows():
                            product = self.db.query(Product).filter(Product.sku == item_row['sku']).first()
                            if not product:
                                continue

                            po_item = PurchaseOrderItem(
                                purchase_order_id=po.id,
                                product_id=product.id,
                                quantity=int(item_row['quantity']),
                                unit_price=float(item_row['unit_price']),
                                total_price=float(item_row['quantity']) * float(item_row['unit_price'])
                            )
                            self.db.add(po_item)

                    results.append({"po_number": po.po_number, "status": "success"})
                except Exception as e:
                    results.append({"po_number": row.get('po_number', 'unknown'), "status": "error", "message": str(e)})
            
            self.db.commit()
            return results
        except Exception as e:
            logger.error(f"Error importing purchase orders: {str(e)}")
            raise 