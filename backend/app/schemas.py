from pydantic import BaseModel
from datetime import datetime
class Product(BaseModel):
    id: int
    name: str
    price: float class ProductList(BaseModel):
        products: list[Product]
class CartItem(BaseModel):
    product_id: int
    quantity: int class CartItems(BaseModel):
        cart_items: list[CartItem]
class OrderItem(BaseModel):
    product_id: int
    quantity: int
class OrderCreate(BaseModel):
    items: list[OrderItem]
class Order(BaseModel):
    id: int
    user_id: int
    status: str
class UserCreate(BaseModel):
    username: str
    password: str
    email: str class Token(BaseModel):
        access_token: str
    token_type: str
class TokenData(BaseModel):
    sub: str | None = None