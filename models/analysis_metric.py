from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from database import Base

class AnalysisMetric(Base):
    __tablename__ = "analysis_metric" 

    metric_id = Column(Integer, primary_key=True, autoincrement=True)  # serial4
    result_id = Column(UUID(as_uuid=True), nullable=False)

    readability_score = Column(Integer)
    reliability_score = Column(Integer)
    financial_risk = Column(Integer)
    coverage_risk = Column(Integer)