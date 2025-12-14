from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

quote_table = Table('quote', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('quote_id', Integer, ForeignKey('quote.id'))
)

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

    def __repr__(self):
        return f'Order(id={self.id}, user_id={self.user_id})'

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f'OrderItem(id={self.id}, order_id={self.order_id})'

quote_table = Table('quote', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('quote_id', Integer, ForeignKey('quote.id'))
)

Base.metadata.create_all(engine)
