from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import crud

# methode for hashing
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")

# variables
SECRET_KEY = "1672adfecd9820e40590795d0eddc773175b28789f0029181bcdc4e25300ce68"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_owner(db: Session, name: str, password: str):
    owner = crud.get_owner_name(db, name)
    if not owner:
        return False
    if not verify_password(password, owner.hashed_password):
        return False
    return owner


def create_acces_token(data: dict):
    to_encode = data.copy()
    expires_data = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_data:
        expire = datetime.utcnow() + expires_data
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
