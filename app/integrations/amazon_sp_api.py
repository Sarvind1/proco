from sp_api.api import Orders, Products, Inventory
from sp_api.base import Marketplaces
from sp_api.auth import AccessTokenClient
from datetime import datetime, timedelta
import logging

from app.core.config import settings

logger = logging.getLogger(__name__)

class AmazonSPAPI:
    def __init__(self):
        self.credentials = {
            "refresh_token": settings.AMAZON_REFRESH_TOKEN,
            "lwa_app_id": settings.AMAZON_CLIENT_ID,
            "lwa_client_secret": settings.AMAZON_CLIENT_SECRET,
            "aws_access_key": settings.AWS_ACCESS_KEY,
            "aws_secret_key": settings.AWS_SECRET_KEY,
            "region": "us-east-1"
        }
        self.marketplace = Marketplaces.US
        self._init_clients()

    def _init_clients(self):
        """Initialize SP-API clients"""
        self.orders_api = Orders(credentials=self.credentials, marketplace=self.marketplace)
        self.products_api = Products(credentials=self.credentials, marketplace=self.marketplace)
        self.inventory_api = Inventory(credentials=self.credentials, marketplace=self.marketplace)

    async def get_orders(self, start_time: datetime = None, end_time: datetime = None):
        """Fetch orders from Amazon"""
        if not start_time:
            start_time = datetime.utcnow() - timedelta(days=1)
        if not end_time:
            end_time = datetime.utcnow()

        try:
            response = self.orders_api.get_orders(
                CreatedAfter=start_time.isoformat(),
                CreatedBefore=end_time.isoformat()
            )
            return response.payload
        except Exception as e:
            logger.error(f"Error fetching orders: {str(e)}")
            raise

    async def get_inventory(self, skus: list):
        """Fetch inventory levels for given SKUs"""
        try:
            response = self.inventory_api.get_inventory_summary_marketplace(
                marketplace_ids=[settings.AMAZON_MARKETPLACE_ID],
                skus=skus
            )
            return response.payload
        except Exception as e:
            logger.error(f"Error fetching inventory: {str(e)}")
            raise

    async def update_inventory(self, sku: str, quantity: int):
        """Update inventory level for a SKU"""
        try:
            response = self.inventory_api.update_inventory(
                sku=sku,
                quantity=quantity
            )
            return response.payload
        except Exception as e:
            logger.error(f"Error updating inventory: {str(e)}")
            raise

    async def get_product_details(self, asins: list):
        """Fetch product details for given ASINs"""
        try:
            response = self.products_api.get_catalog_item(asins)
            return response.payload
        except Exception as e:
            logger.error(f"Error fetching product details: {str(e)}")
            raise

    async def sync_orders(self, db):
        """Sync orders from Amazon to local database"""
        try:
            orders = await self.get_orders()
            # Process orders and update local database
            # Implementation depends on your order model structure
            return orders
        except Exception as e:
            logger.error(f"Error syncing orders: {str(e)}")
            raise

    async def sync_inventory(self, db):
        """Sync inventory levels from Amazon to local database"""
        try:
            # Get all active products with Amazon ASINs
            products = db.query(Product).filter(Product.is_active == True).all()
            skus = [p.sku for p in products]
            
            inventory = await self.get_inventory(skus)
            # Process inventory and update local database
            # Implementation depends on your inventory model structure
            return inventory
        except Exception as e:
            logger.error(f"Error syncing inventory: {str(e)}")
            raise 