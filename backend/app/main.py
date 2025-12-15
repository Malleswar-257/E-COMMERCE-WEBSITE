from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from jose import jwt
from passlib.context import CryptContext
from bcrypt import hashpw, gensalt

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

engine = create_engine('postgresql://user:password@localhost/dbname')
Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

pwd_context = CryptContext(schemes=["bcrypt"])

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = pwd_context.hash(password)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    total = Column(Float)

    def __init__(self, status, total):
        self.status = status
        self.total = total

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    status = Column(String)

    def __init__(self, status):
        self.status = status

Base.metadata.create_all(engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/api/register")
def register(user: User):
    session.add(user)
    session.commit()
    return {"token": jwt.encode({"sub": user.email}, "secret_key", algorithm="HS256")}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = session.query(User).filter(User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        return False
    return {"token": jwt.encode({"sub": user.email}, "secret_key", algorithm="HS256")}

@app.get("/api/products")
def get_products(token: str = Depends(oauth2_scheme)):
    products = session.query(Product).all()
    return {"products": [{"id": product.id, "name": product.name, "price": product.price, "stock": product.stock} for product in products]}

@app.get("/api/products/{product_id}")
def get_product(product_id: int, token: str = Depends(oauth2_scheme)):
    product = session.query(Product).filter(Product.id == product_id).first()
    return {"product": {"id": product.id, "name": product.name, "price": product.price, "stock": product.stock}}

@app.post("/api/cart")
def add_to_cart(product_id: int, quantity: int, token: str = Depends(oauth2_scheme)):
    product = session.query(Product).filter(Product.id == product_id).first()
    if product.stock < quantity:
        return {"error": "Not enough stock"}
    product.stock -= quantity
    session.commit()
    return {"cart": {"products": [{"id": product.id, "name": product.name, "price": product.price, "quantity": quantity}]}}

@app.get("/api/orders")
def get_orders(token: str = Depends(oauth2_scheme)):
    orders = session.query(Order).all()
    return {"orders": [{"id": order.id, "status": order.status, "total": order.total} for order in orders]}

@app.get("/api/orders/{order_id}")
def get_order(order_id: int, token: str = Depends(oauth2_scheme)):
    order = session.query(Order).filter(Order.id == order_id).first()
    return {"order": {"id": order.id, "status": order.status, "total": order.total}}

@app.post("/api/payments")
def make_payment(order_id: int, payment_method: str, token: str = Depends(oauth2_scheme)):
    order = session.query(Order).filter(Order.id == order_id).first()
    payment = Payment(status="paid")
    session.add(payment)
    session.commit()
    return {"payment": {"id": payment.id, "status": payment.status}}, 