from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from models import User

router = APIRouter()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()