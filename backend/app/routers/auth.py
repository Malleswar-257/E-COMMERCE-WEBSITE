from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from app.database import engine
from app.models import User

router = APIRouter()


class RegisterRequest(BaseModel):
    email: str
    phone: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/api/register")
def register(request: RegisterRequest):
    conn = engine.connect()
    result = conn.execute("INSERT INTO users (email, phone, password) VALUES (?, ?, ?)", (request.email, request.phone, request.password))
    conn.close()
    return JSONResponse(content={"message": "User registered successfully"}, status_code=201)


@router.post("/api/login")
def login(request: LoginRequest):
    conn = engine.connect()
    result = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (request.email, request.password))
    user = result.fetchone()
    conn.close()
    if user:
        return JSONResponse(content={"token": "your_token_here"}, status_code=200)
else:
    raise HTTPException(status_code=401, detail="Invalid email or password")