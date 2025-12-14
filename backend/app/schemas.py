from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    password: str
    phone: str

    class Config:
        orm_mode = True

class ProductSchema(BaseModel):
    name: str
    price: float
    stock: int

    class Config:
        orm_mode = True

class OrderSchema(BaseModel):
    user_id: int
    total: float
    status: str

    class Config:
        orm_mode = True

class CartSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True
