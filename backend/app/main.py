from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from typing import List, Optional
from app.settings import settings
from app.models import Base


cors_origins = ["*"]


app = FastAPI(
    title="E-commerce Platform",
    description="A modern, scalable, full-stack e-commerce platform designed to support product listings, cart, checkout, secure payments, order management, and admin dashboards.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations on users"
        },
        {
            "name": "products",
            "description": "Operations on products"
        },
        {
            "name": "cart",
            "description": "Operations on cart"
        },
        {
            "name": "orders",
            "description": "Operations on orders"
        }
    ]
)


origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base.metadata.create_all(bind = engine)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
async def login(request: Request):
    form_data = await request.form()
    email = form_data.get("email")
    password = form_data.get("password")
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if user and user.verify_password(password):
        return JSONResponse(content={"token": user.email})
else:
    raise HTTPException(status_code=401, detail="Invalid email or password")