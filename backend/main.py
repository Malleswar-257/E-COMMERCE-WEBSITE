from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from jose import jwt
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True)

    def __init__(self, user_id: int, product_id: int, quantity: int):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cart_id = Column(Integer, ForeignKey("carts.id"))
    payment_method = Column(String, index=True)
    status = Column(String, index=True)

    def __init__(self, user_id: int, cart_id: int, payment_method: str, status: str):
        self.user_id = user_id
        self.cart_id = cart_id
        self.payment_method = payment_method
        self.status = status

        # Pydantic models
class UserIn(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class ProductIn(BaseModel):
    name: str
    price: float

class ProductOut(BaseModel):
    id: int
    name: str
    price: float

class CartIn(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

class OrderIn(BaseModel):
    user_id: int
    cart_id: int
    payment_method: str
    status: str

class OrderOut(BaseModel):
    id: int
    user_id: int
    cart_id: int
    payment_method: str
    status: str

    # Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# Routes
@app.post("/api/auth/register")
def register(user: UserIn):
    new_user = User(username=user.username, email=user.email, password=user.password)
    db = SessionLocal()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/products")
def read_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products

@app.get("/api/products/{product_id}")
def read_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/api/cart")
def add_item_to_cart(cart: CartIn):
    db = SessionLocal()
    new_cart_item = Cart(user_id=cart.user_id, product_id=cart.product_id, quantity=cart.quantity)
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return new_cart_item

@app.get("/api/cart")
def read_cart():
    db = SessionLocal()
    cart_items = db.query(Cart).all()
    return cart_items

@app.post("/api/orders")
def create_order(order: OrderIn):
    db = SessionLocal()
    new_order = Order(user_id=order.user_id, cart_id=order.cart_id, payment_method=order.payment_method, status=order.status)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.get("/api/orders")
def read_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    return orders))