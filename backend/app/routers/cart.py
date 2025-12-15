from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from app.database import engine
from app.models import Cart

router = APIRouter()


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int


@router.post("/api/cart")
def add_to_cart(request: AddToCartRequest):
    conn = engine.connect()
    result = conn.execute("INSERT INTO cart (product_id, quantity) VALUES (?, ?)", (request.product_id, request.quantity))
    conn.close()
    return JSONResponse(content={"message": "Item added to cart successfully"}, status_code=201)