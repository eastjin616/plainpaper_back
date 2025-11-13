from sqlalchemy import Column, Text , DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base
from sqlalchemy import text

class AnalysisResult(Base):
    __tablename__ = 'analysis_results'

    result_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    document_id = Column(UUID(as_uuid=True), nullable=False)
    model_id = Column(UUID(as_uuid=True), nullable=False)
    summary_Text = Column(Text)
    ai_comment = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))