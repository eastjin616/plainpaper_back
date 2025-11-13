from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base

class AIModelVersion(Base):
    __tablename__ = 'ai_model_versions'

    model_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    model_name = Column(String(200))
    provider = Column(String(100))
    version = Column(String(50))
    description = Column(String(255))