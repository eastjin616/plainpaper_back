from sqlalchemy import Column, Integer , DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base  
from sqlalchemy import text

class Feedback(Base):
    __tablename__ = 'feedbacks'

    feedback_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    member_id = Column(UUID(as_uuid=True), nullable=False)
    document_id = Column(UUID(as_uuid=True), nullable=False)
    rating = Column(Integer, nullable=False)
    comments = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))