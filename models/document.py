from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from database import Base

class Document(Base):
    __tablename__ = 'documents'

    document_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    member_id = Column(UUID(as_uuid=True), nullable=False)
    original_filename = Column(String(255))
    file_path = Column(String(255))
    file_type = Column(String(50))
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default='active')