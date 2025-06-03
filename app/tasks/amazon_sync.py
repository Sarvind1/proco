from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session

from app.worker import celery_app
from app.core.database import SessionLocal
from app.integrations.amazon_sp_api import AmazonSPAPI

logger = logging.getLogger(__name__)

@celery_app.task
def sync_amazon_orders():
    """Sync orders from Amazon"""
    try:
        db = SessionLocal()
        amazon_api = AmazonSPAPI()
        orders = amazon_api.sync_orders(db)
        logger.info(f"Successfully synced {len(orders)} orders from Amazon")
        return {"status": "success", "orders_synced": len(orders)}
    except Exception as e:
        logger.error(f"Error syncing Amazon orders: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()

@celery_app.task
def sync_amazon_inventory():
    """Sync inventory from Amazon"""
    try:
        db = SessionLocal()
        amazon_api = AmazonSPAPI()
        inventory = amazon_api.sync_inventory(db)
        logger.info("Successfully synced inventory from Amazon")
        return {"status": "success", "inventory_synced": True}
    except Exception as e:
        logger.error(f"Error syncing Amazon inventory: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()

@celery_app.task
def update_amazon_inventory(sku: str, quantity: int):
    """Update inventory on Amazon"""
    try:
        amazon_api = AmazonSPAPI()
        result = amazon_api.update_inventory(sku, quantity)
        logger.info(f"Successfully updated inventory for SKU {sku}")
        return {"status": "success", "sku": sku, "quantity": quantity}
    except Exception as e:
        logger.error(f"Error updating Amazon inventory: {str(e)}")
        return {"status": "error", "message": str(e)} 