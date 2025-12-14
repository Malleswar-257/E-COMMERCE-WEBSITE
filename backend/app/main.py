from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.database import database, Base
from app.models import User, Product, Order, Cart
from app.routes import user_router, product_router, order_router, cart_router, admin_router
from app.auth import auth_router
from app.settings import Settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    database.connect()
    Base.metadata.create_all(database.engine)

@app.on_event("shutdown")
def shutdown_event():
    database.disconnect()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(cart_router)
app.include_router(admin_router)
app.include_router(auth_router)