from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from app.models import Product


router = APIRouter(tags=["products"])


@router.post("/products")
async def create_product(product: Product, db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current_user)):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/products")
async def read_products(db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current_user)):
    products = db.query(Product).all()
    return products


@router.get("/products/{product_id}")
async def read_product(product_id: int, db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        return {"error": "Product not found"}
    return product