#! Not sure if it works or not jfix the code if it doesn't work
import jose
from datetime import datetime, timedelta

import jose.jwt
from models import schemas
import os
from utils.envutils import Environment

env = Environment()
secret_key = env.secret_key
ALGORITHM = env.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = env.access_token_expire_minutes
TOKEN_TYPE = env.TOKEN_TYPE
TOKEN_KEY = env.TOKEN_KEY

# Create the access token


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jose.jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return encoded_jwt
