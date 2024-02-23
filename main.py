from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from logger import logger
from deps import get_current_user
import uvicorn
from routers import trial

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting application")
        yield
    finally:
        logger.info("Stopping application")

app = FastAPI(title="Kriyam Vision Project", version="1.0.0", lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET','POST','PUT','DELETE'],
    allow_headers=["*"],
)

# app.include_router(preprocess.router, prefix="/api/v1", tags=["preprocess"], dependencies=[Depends(get_current_user)])
# app.include_router(asr.router, prefix="/api/v1", tags=["asr"], dependencies=[Depends(get_current_user)])
# app.include_router(authenticate.router, prefix="/api/v1")
# app.include_router(trial.router, prefix="/api/v1", dependencies=[Depends(get_current_user)])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)