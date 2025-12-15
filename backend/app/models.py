from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    rating: float

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: int
    total: float
    status: str

    class Config:
        orm_mode = True

class Cart(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    products = relationship("ProductTable", back_populates="user")
    orders = relationship("OrderTable", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"

class ProductTable(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    rating = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserTable", back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name})"

class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float)
    status = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserTable", back_populates="orders")

    def __repr__(self):
        return f"Order(id={self.id}, total={self.total})"

class CartTable(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    product = relationship("ProductTable", back_populates="cart")

    def __repr__(self):
        return f"Cart(id={self.id}, product_id={self.product_id})"