from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return f"User(id={self.id}, email='{self.email}', name='{self.name}')"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    stock = Column(Integer, index=True)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    quantity = Column(Integer, index=True)

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), index=True)
    payment_method = Column(String, index=True)
    status = Column(String, index=True)

    def __init__(self, user_id, cart_id, payment_method, status):
        self.user_id = user_id
        self.cart_id = cart_id
        self.payment_method = payment_method
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, cart_id={self.cart_id}, payment_method='{self.payment_method}', status='{self.status}')"

        # Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
        except Exception as e:
            pass
finally:
    db.close()

    # Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# Authentication
@app.post("/api/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
    

@app.post("/api/auth/register")
def register(user: User):
    db.add(user)
    db.commit()
    return user

    # Product management
@app.get("/api/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/api/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()

    # Cart management
@app.post("/api/cart")
def add_to_cart(cart: Cart, db: Session = Depends(get_db)):
    db.add(cart)
    db.commit()
    return cart

@app.get("/api/cart")
def get_cart(db: Session = Depends(get_db)):
    return db.query(Cart).all()

    # Order management
@app.post("/api/orders")
def create_order(order: Order, db: Session = Depends(get_db)):
    db.add(order)
    db.commit()
    return order

@app.get("/api/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()}))