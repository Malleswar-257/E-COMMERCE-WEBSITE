from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
db_url = settings.DATABASE_URL
echo = False
engine = create_engine(db_url, connect_args={}, echo=echo)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()