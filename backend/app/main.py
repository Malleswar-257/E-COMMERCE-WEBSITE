from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

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

engine = create_engine(os.getenv('DATABASE_URL'))
Base = declarative_base()

# Authentication
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# JWT Settings
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    # Schemas
class UserSchema(BaseModel):
    email: str
    phone: str
    password: str

class ProductSchema(BaseModel):
    name: str
    price: float
    stock: int
    rating: float

class OrderSchema(BaseModel):
    user_id: int
    total: float
    status: str

    # Routes
@app.post("/api/register")
def register(user: UserSchema):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, phone=user.phone, password=hashed_password)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    session.add(new_user)
    session.commit()
    return JSONResponse(content={"token": create_access_token(user.email)}, status_code=201)

@app.post("/api/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user:
        return JSONResponse(content={"error": "Invalid username or password"}, status_code=401)
    if not pwd_context.verify(form_data.password, user.password):
        return JSONResponse(content={"error": "Invalid username or password"}, status_code=401)
    return JSONResponse(content={"token": create_access_token(user.email)}, status_code=200)

@app.get("/api/products")
def get_products():
    session = Session(bind=engine)
    products = session.query(Product).all()
    return JSONResponse(content=[product.__dict__ for product in products], status_code=200)

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    session = Session(bind=engine)
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return JSONResponse(content={"error": "Product not found"}, status_code=404)
    return JSONResponse(content=product.__dict__, status_code=200)

@app.post("/api/cart")
def add_to_cart(product_id: int, quantity: int):
    session = Session(bind=engine)
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return JSONResponse(content={"error": "Product not found"}, status_code=404)
        # Add to cart logic
    return JSONResponse(content={"message": "Product added to cart"}, status_code=200)

@app.post("/api/checkout")
def checkout(payment_method: str, address: str):
    session = Session(bind=engine)
    # Checkout logic
    return JSONResponse(content={"message": "Order created"}, status_code=200)

@app.get("/api/orders")
def get_orders():
    session = Session(bind=engine)
    orders = session.query(Order).all()
    return JSONResponse(content=[order.__dict__ for order in orders], status_code=200)

@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
    session = Session(bind=engine)
    order = session.query(Order).filter(Order.id == order_id).first()
    if not order:
        return JSONResponse(content={"error": "Order not found"}, status_code=404)
    return JSONResponse(content=order.__dict__, status_code=200)

    # Helper functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(username: str):
    session = Session(bind=engine)
    user = session.query(User).filter(User.email == username).first()
    return user
