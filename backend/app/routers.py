from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.main import oauth2_scheme, pwd_context
from app.models import User, Product, Order, Cart
from app.schemas import UserSchema, ProductSchema, OrderSchema, CartSchema
from sqlalchemy.orm import Session
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv

load_dotenv()

router = APIRouter()

@router.post("/register")
def register(user: UserSchema):
    user_obj = User(email=user.email, password=pwd_context.hash(user.password), phone=user.phone)
    Session.add(user_obj)
    Session.commit()
    return JSONResponse(content={"token": jwt.encode({"sub": user.email}, getenv('SECRET_KEY'), algorithm="HS256")}, media_type="application/json")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = Session.query(User).filter(User.email == form_data.username).first()
    if not user:
        return JSONResponse(content={"error": "Invalid email or password"}, media_type="application/json", status_code=401)
    if not pwd_context.verify(form_data.password, user.password):
        return JSONResponse(content={"error": "Invalid email or password"}, media_type="application/json", status_code=401)
    return JSONResponse(content={"token": jwt.encode({"sub": user.email}, getenv('SECRET_KEY'), algorithm="HS256")}, media_type="application/json")

@router.get("/products")
def get_products(token: str = Depends(oauth2_scheme)):
    products = Session.query(Product).all()
    return JSONResponse(content=[ProductSchema.from_orm(product).dict() for product in products], media_type="application/json")

@router.get("/products/{id}")
def get_product(id: int, token: str = Depends(oauth2_scheme)):
    product = Session.query(Product).filter(Product.id == id).first()
    if not product:
        return JSONResponse(content={"error": "Product not found"}, media_type="application/json", status_code=404)
    return JSONResponse(content=ProductSchema.from_orm(product).dict(), media_type="application/json")

@router.post("/cart")
def add_to_cart(cart: CartSchema, token: str = Depends(oauth2_scheme)):
    user = Session.query(User).filter(User.email == jwt.decode(token, getenv('}
)))