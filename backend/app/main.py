from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from pydantic import BaseModel
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = FastAPI()

origins = [
    "*",
]

cors = CORSMiddleware(
    app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(getenv('DATABASE_URL'))
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
