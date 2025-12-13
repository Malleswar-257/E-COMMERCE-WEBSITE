from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create