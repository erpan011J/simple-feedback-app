from sqlalchemy import Column, Integer, String
from ..database.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
