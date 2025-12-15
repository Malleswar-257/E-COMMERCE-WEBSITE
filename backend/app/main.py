from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import sqlite3
from app.config import settings
from app.database import engine
from app.routers import auth, cart, orders, products, admin

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(products.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the e-commerce platform"}, 