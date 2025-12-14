from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __init__(self, email, password, phone):
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return f"User(id={self.id}, email='{self.email}', phone='{self.phone}')"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    def __init__(self, name, price, stock, rating):
        self.name = name
        self.price = price
        self.stock = stock
        self.rating = rating

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock}, rating={self.rating})"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, nullable=False)

    user = relationship("User", backref="orders")

    def __init__(self, user_id, status):
        self.user_id = user_id
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, order_date='{self.order_date}', status='{self.status}')"

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", backref="cart")

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"Cart(id={self.id}, product_id={self.product_id}, quantity={self.quantity})"