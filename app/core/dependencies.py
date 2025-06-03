from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from fastapi import Depends, HTTPException, status

# Dependency to get DB session

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get current user (placeholder)
def get_current_user():
    # In a real app, implement authentication here
    return {"username": "admin", "is_active": True} 