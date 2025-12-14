from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from app.settings import Settings

engine = create_engine(Settings().DATABASE_URL)
Base = declarative_base()
database = scoped_session(sessionmaker(bind=engine))