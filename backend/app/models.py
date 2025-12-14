from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(BaseModel):
    id: int
    email: str
    password: str
    phone: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class Cart(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    total: float
    status: str
