from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List
from app.database import engine
from app.database import SessionLocal
from app.database import Base
from app.database import User
from app.database import Product
from app.database import Cart
from app.database import Order
from app.database import OrderItem
from app.auth import AuthHandler
from app.auth import get_user
from app.auth import get_current_user
from app.auth import get_current_active_user
from app.auth import get_current_active_admin
from app.crud import crud
from app.schemas import schemas
from app.utils import utils

app = FastAPI()

origins = [
    "*"
]

cors = CORSMiddleware(
    app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the E-COMMERCE-WEBSITE API!"}, 