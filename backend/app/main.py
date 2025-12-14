from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from typing import List
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv

load_dotenv()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# Database configuration
DATABASE_URL = getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Security configuration
SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ALGORITHM')

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Define models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    password = Column(String)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    total = Column(Float)

    # Define schemas
class UserSchema(BaseModel):
    email: str
    phone: str
    password: str

class ProductSchema(BaseModel):
    name: str
    price: float
    stock: int

class CartSchema(BaseModel):
    product_id: int
    quantity: int

class OrderSchema(BaseModel):
    total: float

    # Define routes
@app.post("/api/register")
def register(user: UserSchema):
# Register a new user
    db = SessionLocal()
    user.password = pwd_context.hash(user.password)
    db.add(User(**user.dict()))
    db.commit()
    return {"token": jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)}

@app.post("/api/login")
def login(user: UserSchema):
# Log in a user
    db = SessionLocal()
    user_db = db.query(User).filter(User.email == user.email).first()
    if not user_db or not pwd_context.verify(user.password, user_db.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)}

@app.get("/api/products")
def get_products():
# Get all products
    db = SessionLocal()
    products = db.query(Product).all()
    return {"products": [product.name for product in products]}

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
# Get a product by ID
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product.name}

@app.post("/api/cart")
def add_to_cart(cart: CartSchema):
# Add an item to cart
    db = SessionLocal()
    cart_db = Cart(user_id=1, product_id=cart.product_id, quantity=cart.quantity)
    db.add(cart_db)
    db.commit()
    return {"cart": [cart.product_id]}

@app.get("/api/cart")
def get_cart():
# Get cart items
    db = SessionLocal()
    cart = db.query(Cart).filter(Cart.user_id == 1).all()
    return {"cart": [item.product_id for item in cart]}

@app.post("/api/checkout")
def checkout(order: OrderSchema):
# Complete checkout
    db = SessionLocal()
    order_db = Order(user_id=1, total=order.total)
    db.add(order_db)
    db.commit()
    return {"order": order_db.id}

@app.get("/api/orders")
def get_orders():
# Get all orders
    db = SessionLocal()
    orders = db.query(Order).filter(Order.user_id == 1).all()
    return {"orders": [order.id for order in orders]}

@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
# Get an order by ID
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"order": order.id}, 