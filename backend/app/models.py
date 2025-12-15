from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    status = Column(String)
    total = Column(Float)

    def __init__(self, status, total):
        self.status = status
        self.total = total

class Payment(Base):
    __tablename__