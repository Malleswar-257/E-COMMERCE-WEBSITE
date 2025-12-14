from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.main import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)
    orders = relationship("Order", backref="user")
    cart = relationship("Cart", backref="user")

    def __init__(self, email, password, phone):
        self.email = email
        self.password = password
        self.phone = phone

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    cart = relationship("Cart", backref="product")

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Float)
    status = Column(String)

    def __init__(self, user_id, total, status):
        self.user_id = user_id
        self.total = total
        self.status = status

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
