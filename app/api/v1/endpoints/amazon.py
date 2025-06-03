from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.amazon import AmazonResponse
from typing import List

router = APIRouter()

@router.get("/amazon/", response_model=List[AmazonResponse])
def list_amazon_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    List Amazon data (placeholder implementation).
    """
    # Placeholder: return empty list
    return [] 