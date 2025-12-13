from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from jose import jwt, JWTError
from typing import List
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Initialize SQLAlchemy
engine = create_engine(
    "postgresql://user:password@localhost/dbname",
    echo=T,rue


    # Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions.
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

        # Define the Product model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    def __init__(self, name, description, price, stock, rating):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.rating = rating

        # Define the Cart model
class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    user = relationship("User", backref="carts")
    product = relationship("Product", backref="carts")

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

        # Define the Order model
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    payment_method = Column(String, nullable=False)

    cart = relationship("Cart", backref="orders")

    def __init__(self, cart_id, payment_method):
        self.cart_id = cart_id
        self.payment_method = payment_method

        # Create all tables in the engine
Base.metadata.create_all(engine)

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define the password context
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Define the JWT secret key
SECRET_KEY = "secret_key"

# Define the JWT algorithm
ALGORITHM = "HS256"

# Define the access token expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define the authentication route
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"}, media_type="application/json")

    # Define the registration route
@app.post("/register")
def register_user(user: User):
    db = Session()
    db.add(user)
    db.commit()
    return JSONResponse(content={"message": "User created successfully"}, media_type="application/json")

    # Define the product route
@app.get("/products")
def get_products():
    db = Session()
    products = db.query(Product).all()
    return JSONResponse(content=[product.__dict__ for product in products], media_type="application/json")

    # Define the cart route
@app.post("/cart")
def add_to_cart(cart: Cart):
    db = Session()
    db.add(cart)
    db.commit()
    return JSONResponse(content={"message": "Item added to cart successfully"}, media_type="application/json")

    # Define the order route
@app.post("/orders")
def create_order(order: Order):
    db = Session()
    db.add(order)
    db.commit()
    return JSONResponse(content={"message": "Order created successfully"}, media_type="application/json")

    # Define the authentication function
def authenticate_user(username: str, password: str):
    db = Session()
    user = db.query(User).filter(User.email == username).first()
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

    # Define the access token creation function
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

    # Define the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],))))