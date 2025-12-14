from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
def get_db():
    db = SessionLocal()
    try:
        except Exception as e:
            pass
        yield db
finally:
    db.close()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum('admin', 'user'))
class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)
class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    status = Column(Enum('pending', 'confirmed', 'cancelled'))