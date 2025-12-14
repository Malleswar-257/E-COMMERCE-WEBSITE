from sqlalchemy.orm import Session
from app import models, schemas
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        for attr, value in user.dict(exclude_unset=True).items():
            setattr(db_user, attr, value)
        db.commit()
        db.refresh(db_user)
    return db_user
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return False
    return True
def create_hotel(db: Session, hotel: schemas.HotelCreate):
    db_hotel = models.Hotel(name=hotel.name, address=hotel.address, phone=hotel.phone, email=hotel.email)
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel
def get_hotels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()
def get_hotel(db: Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
def update_hotel(db: Session, hotel_id: int, hotel: schemas.HotelUpdate):
    db_hotel = get_hotel(db, hotel_id=hotel_id)
    if db_hotel:
        for attr, value in hotel.dict(exclude_unset=True).items():
            setattr(db_hotel, attr, value)
        db.commit()
        db.refresh(db_hotel)
    return db_hotel
def delete_hotel(db: Session, hotel_id: int):
    db_hotel = get_hotel(db, hotel_id=hotel_id)
    if db_hotel:
        db.delete(db_hotel)
        db.commit()
def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(user_id=booking.user_id, hotel_id=booking.hotel_id, check_in=booking.check_in, check_out=booking.check_out, status=booking.status)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()
def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()
def update_booking(db: Session, booking_id: int, booking: schemas.BookingUpdate):
    db_booking = get_booking(db, booking_id=booking_id)
    if db_booking:
        for attr, value in booking.dict(exclude_unset=True).items():
            setattr(db_booking, attr, value)
        db.commit()
        db.refresh(db_booking)
    return db_booking
def delete_booking(db: Session, booking_id: int):
    db_booking = get_booking(db, booking_id=booking_id)
    if db_booking:
        db.delete(db_booking)
        db.commit()