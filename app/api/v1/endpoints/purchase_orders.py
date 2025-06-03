from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.purchase_order import PurchaseOrderResponse
from typing import List

router = APIRouter()

@router.get("/purchase-orders/", response_model=List[PurchaseOrderResponse])
def list_purchase_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    List purchase orders (placeholder implementation).
    """
    # Placeholder: return empty list
    return [] 