from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel
from database import SessionLocal
from models.member import Member
from models.email_verification import EmailVerification  
from utils.password import hash_password # 비밀번호 해싱 함수 임포트

router = APIRouter(prefix="", tags=["Register"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):

    # 1️⃣ 이미 가입된 이메일인지 확인
    existing = db.query(Member).filter(Member.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")

    # 2️⃣ 이메일 인증 여부 확인
    verification = (
        db.query(EmailVerification)
        .filter(EmailVerification.email == request.email)
        .first()
    )

    if not verification or not verification.verified:
        raise HTTPException(status_code=400, detail="이메일 인증이 완료되지 않았습니다.")

    # 3️⃣ 최종 가입
    new_user = Member(
        member_id=uuid4(),
        name=request.name,
        email=request.email,
        password=hash_password(request.password),  # 비밀번호 해싱 함수 사용 가정
        create_at=datetime.utcnow()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 4️⃣ 가입 완료 후 인증 기록 삭제 (선택)
    db.delete(verification)
    db.commit()

    return {"message": "회원가입 성공", "member_id": str(new_user.member_id)}