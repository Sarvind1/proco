from fastapi import APIRouter

from app.api.v1.endpoints import auth, products, inventory, purchase_orders, suppliers, amazon

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
api_router.include_router(purchase_orders.router, prefix="/purchase-orders", tags=["purchase orders"])
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(amazon.router, prefix="/amazon", tags=["amazon integration"]) 