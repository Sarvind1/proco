from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.supplier import SupplierResponse
from typing import List

router = APIRouter()

@router.get("/suppliers/", response_model=List[SupplierResponse])
def list_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    List suppliers (placeholder implementation).
    """
    # Placeholder: return empty list
    return [] 