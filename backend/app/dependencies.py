from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.main import oauth2_scheme


def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()


async def get_current_user(token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    user = db.query(User).filter(User.email == token).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user