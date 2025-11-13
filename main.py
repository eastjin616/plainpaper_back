from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, SessionLocal 
from models import *
from routers import auth

app = FastAPI()

# -----------------------------------------
# 🔥 CORS 설정은 FastAPI(app) 선언 직후에 넣는다
# -----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

#라우터 등록
app.include_router(auth.router)
