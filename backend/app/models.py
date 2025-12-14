from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User(id={self.id}, email={self.email})'

    def __str__(self):
        return f'User(id={self.id}, email={self.email})'


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

    def __repr__(self):
        return f'Product(id={self.id}, name={self.name})'

    def __str__(self):
        return f'Product(id={self.id}, name={self.name})'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    total = Column(Float)
    status = Column(String)

    def __init__(self, total, status):
        self.total = total
        self.status = status

    def __repr__(self):
        return f'Order(id={self.id}, total={self.total})'

    def __str__(self):
        return f'Order(id={self.id}, total={self.total})'
