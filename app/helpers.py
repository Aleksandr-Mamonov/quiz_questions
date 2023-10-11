import requests

from . import models
from . import schemas
from sqlalchemy.orm import Session


def get_questions_from_public_api(count: int = 1):
    r = requests.get(f"https://jservice.io/api/random?count={count}")
    return r.json()


def get_question_from_db_by_id(db: Session, question_id: int):
    return (
        db.query(models.Question)
        .filter(models.Question.question_id == question_id)
        .first()
    )


def add_question_to_db(db: Session, question: schemas.CreateQuestionSchema):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
