import logging
from pathlib import Path
import os

from app.worker import celery_app
from app.core.database import SessionLocal
from app.integrations.csv_import import CSVImporter

logger = logging.getLogger(__name__)

@celery_app.task
def import_products_csv(file_path: str):
    """Import products from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        db = SessionLocal()
        importer = CSVImporter(db)
        results = importer.import_products(file_path)
        
        success_count = sum(1 for r in results if r["status"] == "success")
        error_count = len(results) - success_count
        
        logger.info(f"Successfully imported {success_count} products, {error_count} errors")
        return {
            "status": "success",
            "total": len(results),
            "success": success_count,
            "errors": error_count,
            "details": results
        }
    except Exception as e:
        logger.error(f"Error importing products from CSV: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()

@celery_app.task
def import_inventory_csv(file_path: str):
    """Import inventory movements from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        db = SessionLocal()
        importer = CSVImporter(db)
        results = importer.import_inventory(file_path)
        
        success_count = sum(1 for r in results if r["status"] == "success")
        error_count = len(results) - success_count
        
        logger.info(f"Successfully imported {success_count} inventory movements, {error_count} errors")
        return {
            "status": "success",
            "total": len(results),
            "success": success_count,
            "errors": error_count,
            "details": results
        }
    except Exception as e:
        logger.error(f"Error importing inventory from CSV: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close()

@celery_app.task
def import_purchase_orders_csv(file_path: str):
    """Import purchase orders from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        db = SessionLocal()
        importer = CSVImporter(db)
        results = importer.import_purchase_orders(file_path)
        
        success_count = sum(1 for r in results if r["status"] == "success")
        error_count = len(results) - success_count
        
        logger.info(f"Successfully imported {success_count} purchase orders, {error_count} errors")
        return {
            "status": "success",
            "total": len(results),
            "success": success_count,
            "errors": error_count,
            "details": results
        }
    except Exception as e:
        logger.error(f"Error importing purchase orders from CSV: {str(e)}")
        return {"status": "error", "message": str(e)}
    finally:
        db.close() 