from sqlalchemy import create_engine
from app.models import Base

engine = create_engine('postgresql://user:password@host:port/dbname')
Base.metadata.create_all(engine)