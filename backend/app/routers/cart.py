from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from app.models import Cart


router = APIRouter(tags=["cart"])


@router.post("/cart")
async def create_cart(cart: Cart, db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current)
)