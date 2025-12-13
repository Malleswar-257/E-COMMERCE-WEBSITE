from fastapi import FastAPI, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth_utils
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
@app.post("/api/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
@app.post("/api/login", response_model=schemas.Token)
def login_for_access_token(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = auth_utils.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_utils.create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}
@app.get("/api/products", response_model=schemas.ProductList)
def get_products(db: Session = Depends(get_db)):
    products = crud.get_products(db=db)
    return {'products': products}
@app.get("/api/cart/{user_id}", response_model=schemas.CartItems)
def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart_items = crud.get_cart_items_by_user_id(db, user_id=user_id)
    return {'cart_items': cart_items}
@app.post("/api/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user=Depends(auth_utils.get_current_active_user)):
    order_items = [{'product_id': item.product_id, 'quantity': item.quantity} for item in order.items]
    return crud.create_order(db=db, user=current_user, items=order_items)