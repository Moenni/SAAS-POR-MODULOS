from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_user, get_all_users
from schemas import UserCreate, UserOut
from typing import List

router = APIRouter(prefix="/users", tags=["users"])


# dependency para obtener la session de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """Crea un usuario usando un modelo Pydantic UserCreate."""
    return create_user(db, name=user.name, email=user.email)


@router.get("/", response_model=List[UserOut])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)