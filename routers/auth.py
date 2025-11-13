from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.member import Member
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 회원가입 요청 바디
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    # 이메일 중복 체크
    existing = db.query(Member).filter(Member.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")

    # 새 유저 생성
    new_user = Member(
        member_id=uuid4(),
        name=request.name,
        email=request.email,
        password=request.password,   # → 나중에 반드시 bcrypt로 암호화해야 함
        create_at=datetime.utcnow()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "회원가입 성공", "member_id": str(new_user.member_id)}