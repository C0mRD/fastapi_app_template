from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi import APIRouter
from uuid import uuid4
from jose import jwt
from models import TokenPayload, AuthenticateModel, Loginrequest
from datetime import datetime, timedelta

from utils import (
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY,
    create_access_token,
    create_refresh_token,
    verify_password,
    get_hashed_password
)

router = APIRouter()

@router.post("/swaggerlogin", response_model=AuthenticateModel)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint to authenticate a user and generate an API key or access token.

    :param username: Username for authentication\n
    :param password: Password for authentication\n
    :return: Access token
    """
    if verify_password(form_data.password, get_hashed_password("geogo#foxivision")):
        access_token_expires = timedelta(minutes=30)
        refresh_token_expires = timedelta(minutes=90)
        access_token = create_access_token(form_data.username)
        refresh_token = create_refresh_token(form_data.username)
        return {
            "access_token": access_token,
            # "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/login", response_model=AuthenticateModel)
async def login(form_data: Loginrequest):
    """
    Endpoint to authenticate a user and generate an API key or access token.

    :param username: Username for authentication\n
    :param password: Password for authentication\n
    :return: Access token
    """
    username = form_data.username
    password = form_data.password

    if verify_password(password, get_hashed_password("geogo#foxivision")):
        access_token_expires = timedelta(minutes=30)
        refresh_token_expires = timedelta(minutes=90)
        access_token = create_access_token(username)
        refresh_token = create_refresh_token(username)
        return {
            "access_token": access_token,
            # "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )