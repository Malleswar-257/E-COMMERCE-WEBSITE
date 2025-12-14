from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
class UserUpdate(BaseModel):
    name: str = None
class HotelCreate(BaseModel):
    name: str
    address: str
    phone: str
    email: str
class HotelUpdate(BaseModel):
    name: str = None
class BookingCreate(BaseModel):
    user_id: int
    hotel_id: int
    check_in: datetime.datetime
    check_out: datetime.datetime
    status: str
class BookingUpdate(BaseModel):
    user_id: int = None
class Token(BaseModel):
    access_token: str
token_type: str