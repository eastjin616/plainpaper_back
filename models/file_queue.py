from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base  
from sqlalchemy import text

class FileQueue(Base):
    __tablename__ = 'file_queue'

    queue_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    member_id = Column(UUID(as_uuid=True), nullable=False)
    file_name = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default='pending')
    start_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    finished_at = Column(DateTime)
    error_message = Column(Text)
    