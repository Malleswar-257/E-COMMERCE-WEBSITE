from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from typing import List

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    cart = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")

    # Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)

    cart = relationship("Cart", back_populates="product")

    # Cart model
class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, index=True)

    user = relationship("User", back_populates="cart")
    product = relationship("Product", back_populates="cart")

    # Order model
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cart_id = Column(Integer, ForeignKey("cart.id"))
    status = Column(String, index=True)

    user = relationship("User", back_populates="orders")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

    # JWT configuration
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

    # JWT token data
class TokenData(BaseModel):
    email: str

    # Password context
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

    # Get password hash
def get_password_hash(password):
    return pwd_context.hash(password)

    # Get user
def get_user(db, email: str):
    return db.query(User).filter(User.email == email).first()

    # Authenticate user
def authenticate_user(db, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

    # Create access token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

    # Get current user
def get_current_user(db, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

    # FastAPI application
app = FastAPI()

# Dependency for getting database session
def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

    # Dependency for getting current user
async def get_current_active_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(db, token)
    if not current_user:
        raise HTTPException(status_code=401, detail="Inactive user")
    return current_user

    # User registration endpoint
@app.post("/api/auth/register", response_model=Token)
async def register_user(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user(db, email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(password)
    db_user = User(email=email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": db_user.email}, expires_delta=access_token_expires
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
    

        # User login endpoint
@app.post("/api/auth/login", response_model=Token)
async def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=)))