from sqlalchemy import Column, String, DateTime, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base

class KeywordHighlight(Base):
    __tablename__ = 'keyword_highlights'

    keyword_id = Column(Integer, primary_key=True, autoincrement=True)
    result_id = Column(UUID(as_uuid=True), nullable=False)
    keyword = Column(String(100))
    category = Column(String(100))
    description = Column(Text)
    highlight_Text = Column(Text)
