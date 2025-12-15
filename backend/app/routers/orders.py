from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from app.database import engine
from app.models import Order

router = APIRouter()


class CreateOrderRequest(BaseModel):
    cart: List[dict]


@router.post("/api/orders")
def create_order(request: CreateOrderRequest):
    conn = engine.connect()
    result = conn.execute("INSERT INTO orders (status, total) VALUES (?, ?)", ("pending", 0.0))
    order_id = result.lastrowid
    for item in request.cart:
        conn.execute("INSERT INTO cart (order_id, product_id, quantity) VALUES (?, ?, ?)", (order_id, item['}'
]
))