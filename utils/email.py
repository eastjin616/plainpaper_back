import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.naver.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 465))

def send_verification_email(to_email: str, verification_code: str):
    subject = "Plainpaper 이메일 인증 코드"
    body = f"""
    안녕하세요. Plainpaper 이메일 인증 안내입니다.

    아래 코드를 입력해주세요.

    인증 코드: {verification_code}

    감사합니다.
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_EMAIL
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, to_email, msg.as_string())

        print(f"[EMAIL SENT] {to_email}")

    except Exception as e:
        print(f"[EMAIL ERROR] {e}")