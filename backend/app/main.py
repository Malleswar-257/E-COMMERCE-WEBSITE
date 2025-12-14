from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import engine, session
from app.routers import products, orders, cart, users, login

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(cart.router)
app.include_router(users.router)
app.include_router(login.router)