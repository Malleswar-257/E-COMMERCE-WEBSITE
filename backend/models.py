from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional

engine = create_engine(getenv('DATABASE_URL'))
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String, nullable=True)

    def __init__(self, email=None, password=None, phone=None):
        self.email = email
        self.password = pwd_context.hash(password)
        self.phone = phone

    def check_password(self, password):
        return pwd_context.verify(password, self.password)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, phone={self.phone})"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    stock = Column(Integer)

    def __init__(self, name=None, price=None, stock=None):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock})"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    total = Column(Float)
    status = Column(String)

    def __init__(self, user_id=None, total=None, status=None):
        self.user_id = user_id
        self.total = total
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, total={self.total}, status={self.status})"

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer)

    def __init__(self, user_id=None, product_id=None, quantity=None):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})"

Base.metadata.create_all(bind=engine)