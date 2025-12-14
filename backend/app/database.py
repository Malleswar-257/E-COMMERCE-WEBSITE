from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import List
from app.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    products = relationship("Product", backref="owner")

    cart = relationship("Cart", backref="owner")

    orders = relationship("Order", backref="owner")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    stock = Column(Integer, index=True)
    rating = Column(Float, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    order_date = Column(Date, index=True)
    total = Column(Float, index=True)
    status = Column(Enum("pending", "shipped", "delivered", name="status"))

    owner_id = Column(Integer, ForeignKey("users.id"))

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True)

Base.metadata.create_all(bind=engine)