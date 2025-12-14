from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic_settings import BaseSettings
from app import crud, schemas, models
db = SessionLocal()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
settings = Settings()
def get_db():
    try:
        except Exception as e:
            pass
        db = SessionLocal()
        yield db
finally:
    db.close()
@app.post("/api/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
@app.get("/api/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users
@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.put("/api/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)
@app.post("/api/hotels", response_model=schemas.Hotel)
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    return crud.create_hotel(db=db, hotel=hotel)
@app.get("/api/hotels", response_model=list[schemas.Hotel])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels = crud.get_hotels(db=db, skip=skip, limit=limit)
    return hotels
@app.get("/api/hotels/{hotel_id}", response_model=schemas.Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = crud.get_hotel(db=db, hotel_id=hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel
@app.put("/api/hotels/{hotel_id}", response_model=schemas.Hotel)
def update_hotel(hotel_id: int, hotel: schemas.HotelUpdate, db: Session = Depends(get_db)):
    return crud.update_hotel(db=db, hotel_id=hotel_id, hotel=hotel)
@app.delete("/api/hotels/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    crud.delete_hotel(db=db, hotel_id=hotel_id)
@app.post("/api/bookings", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)
@app.get("/api/bookings", response_model=list[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db=db, skip=skip, limit=limit)
    return bookings
@app.get("/api/bookings/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.get_booking(db=db, booking_id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
@app.put("/api/bookings/{booking_id}", response_model=schemas.Booking)
def update_booking(booking_id: int, booking: schemas.BookingUpdate, db: Session = Depends(get_db)):
    return crud.update_booking(db=db, booking_id=booking_id, booking=booking)
@app.delete("/api/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    crud.delete_booking(db=db, booking_id=booking_id)
@app.post("/api/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
@app.get("/api/logout")
def logout(token: str = Depends(oauth2_scheme)):
    return {}