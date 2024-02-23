from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import dotenv
import os

router = APIRouter()

@router.get("/trial")
async def trial():
    return JSONResponse(content=jsonable_encoder({"message": "Hello World"}))