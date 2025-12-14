from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from app.database import database
from app.models import User, Product, Order, Cart
from app.auth import get_current_user

user_router = APIRouter()
product_router = APIRouter()
order_router = APIRouter()
cart_router = APIRouter()
admin_router = APIRouter()

@user_router.post("/api/register")
def register_user(user: UserSchema):
    user = User(**user.dict())
    database.add(user)
    database.commit()
    return JSONResponse(content={"message": "User created successfully"}, status_code=201)

@user_router.post("/api/login")
def login_user(user: UserSchema):
    user = database.query(User).filter(User.email == user.email).first()
    if user and user.password == user.password:
        return JSONResponse(content={"token": "token", "user_id": user.id}, status_code=200)
else:
    raise HTTPException(status_code=401, detail="Invalid email or password")

@product_router.get("/api/products")
def get_products():
    products = database.query(Product).all()
    return JSONResponse(content=[product.__dict__ for product in products], status_code=200)

@product_router.get("/api/products/{product_id}")
def get_product(product_id: int):
    product = database.query(Product).filter(Product.id == product_id).first()
    if product:
        return JSONResponse(content=product.__dict__, status_code=200)
else:
    raise HTTPException(status_code=404, detail="Product not found")

@cart_router.post("/api/products/{product_id}/add-to-cart")
def add_to_cart(product_id: int, quantity: int):
    cart = Cart(product_id=product_id, quantity=quantity)
    database.add(cart)
    database.commit()
    return JSONResponse(content={"cart_id": cart.id, "product_id": product_id, "quantity": quantity}, status_code=201)

@order_router.post("/api/checkout")
def checkout(order: OrderSchema):
    order = Order(**order.dict())