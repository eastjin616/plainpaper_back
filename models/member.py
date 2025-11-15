from sqlalchemy import Column, String, Boolean,DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from database import Base

class Member(Base):
    __tablename__ = 'member'

    member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


    create_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)