from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from database import Base, engine
from models import *

# 🔥 라우터 import (이름 절대 겹치지 않게!)
from routers.auth import router as auth_router
from routers.register import router as register_router
from routers.login import router as login_router

# 모델 import
import models.ai_model_version
import models.analysis_metric
import models.analysis_result
import models.document
import models.feedback
import models.file_queue
import models.keyword_highlight
import models.member
import models.email_verification

load_dotenv()

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 🔥 라우터 등록 (딱 1번씩만)
app.include_router(auth_router)
app.include_router(register_router)
app.include_router(login_router)

# -----------------------------------------
# CORS 설정
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