from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from app.models import User, Product, Order, Cart
from app.database import engine, SessionLocal
from app.routers import auth, products, orders, admin
from app.settings import Settings

settings = Settings()

app = FastAPI(
    title="E-commerce API",
    description="API for e-commerce platform",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "auth",
            "description": "Authentication endpoints"
        },
        {
            "name": "products",
            "description": "Product endpoints"
        },
        {
            "name": "orders",
            "description": "Order endpoints"
        },
        {
            "name": "admin",
            "description": "Admin endpoints"
        }
    ]
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(admin.router)

origins = [
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await engine.dispose()
    await engine.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await engine.dispose()