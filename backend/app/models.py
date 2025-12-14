from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

    orders = relationship("Order", backref="user")

    def __init__(self, email, password, phone):
        self.email = email
        self.password = password
        self.phone = phone

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    carts = relationship("Cart", backref="product")

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum("pending", "shipped", "delivered"))
    total = Column(Float)

    user = relationship("User", backref="orders")

    def __init__(self, user_id, status, total):
        self.user_id = user_id
        self.status = status
        self.total = total

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    product = relationship("Product", backref="carts")

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    phone: str

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class OrderSchema(BaseModel):
    id: int
    user_id: int
    status: str
    total: float

class CartSchema(BaseModel):
    id: int
    product_id: int
    quantity: int