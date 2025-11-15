from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.email_verification import EmailVerification
import random
from pydantic import BaseModel
from utils.email import send_verification_email

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SendCodeRequest(BaseModel):
    email: str

class VerifyCodeRequest(BaseModel):
    email: str
    verification_code: str


@router.post("/send-code")
def send_code(request: SendCodeRequest, db: Session = Depends(get_db)):
    email = request.email

    # 기존 기록 삭제 (재발급 대비)
    existing = db.query(EmailVerification).filter(EmailVerification.email == email).first()
    if existing:
        db.delete(existing)
        db.commit()

    # 새 인증코드 생성 & 저장
    code = str(random.randint(100000, 999999))
    new_record = EmailVerification(email=email, code=code)
    db.add(new_record)
    db.commit()

    send_verification_email(email, code)

    return {"message": "인증코드 발송 완료"}


@router.post("/verify-code")
def verify_code(request: VerifyCodeRequest, db: Session = Depends(get_db)):
    record = db.query(EmailVerification).filter(EmailVerification.email == request.email).first()

    if not record:
        raise HTTPException(status_code=400, detail="인증 요청이 없습니다.")

    if record.code != request.verification_code:
        raise HTTPException(status_code=400, detail="잘못된 인증코드")

    record.verified = True
    db.commit()

    return {"message": "이메일 인증 완료"}