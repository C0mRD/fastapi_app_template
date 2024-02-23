from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from models import TokenPayload, SystemUser

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/v1/swaggerlogin",
    scheme_name="JWT"
)

auth_data = {
    "id": 1,
    "username": "geogo@admin",
    "email": "geogo#foxivision"
}

async def get_current_user(token: str = Depends(reuseable_oauth)) -> SystemUser:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # cursor = var.conn.cursor(dictionary=True)
    # query = "SELECT * FROM customer WHERE phonenumber = %s"
    # cursor.execute(query, (token_data.sub,))
    # customer = cursor.fetchone()
    
    if token_data.sub != auth_data["username"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    
    user = SystemUser(
        id=auth_data['id'],
        username=auth_data['username'],
        email=auth_data['email']
    )
    
    return user