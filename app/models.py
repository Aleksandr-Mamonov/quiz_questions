from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
