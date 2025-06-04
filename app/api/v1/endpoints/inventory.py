from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.product import Product, InventoryMovement
from app.schemas.product import InventoryMovementCreate, InventoryMovementResponse

router = APIRouter()

@router.get("/", response_model=List[InventoryMovementResponse])
async def list_inventory_movements(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    List inventory movements
    """
    movements = db.query(InventoryMovement).offset(skip).limit(limit).all()
    return movements

@router.post("/", response_model=InventoryMovementResponse)
async def create_inventory_movement(
    *,
    db: Session = Depends(get_db),
    movement_in: InventoryMovementCreate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Create new inventory movement
    """
    # Verify product exists
    product = db.query(Product).filter(Product.id == movement_in.product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Create movement
    movement = InventoryMovement(**movement_in.dict())
    db.add(movement)
    
    # Update product quantity based on movement type
    if movement_in.movement_type in ['purchase', 'return']:
        product.quantity += movement_in.quantity
    elif movement_in.movement_type in ['sale', 'adjustment']:
        # For adjustment, allow negative quantities
        if movement_in.movement_type == 'sale' and product.quantity < movement_in.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient stock for sale"
            )
        product.quantity -= movement_in.quantity
    
    db.commit()
    db.refresh(movement)
    return movement