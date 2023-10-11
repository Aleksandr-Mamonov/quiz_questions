from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from . import schemas


from .helpers import (
    get_questions_from_public_api,
    get_question_from_db_by_id,
    add_question_to_db,
)
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/quiz/api/v1.0/save_quiz_questions")
def write_questions_to_db(
    questions_request: schemas.QuestionsRequestSchema, db: Session = Depends(get_db)
):
    questions_number = questions_request.questions_num
    questions = get_questions_from_public_api(count=questions_number)
    for question_dict in questions:
        question_is_already_in_db = get_question_from_db_by_id(
            db=db, question_id=question_dict["id"]
        )
        while question_is_already_in_db:
            question_dict = get_questions_from_public_api(count=1)[0]
            question_is_already_in_db = get_question_from_db_by_id(
                db=db, question_id=question_dict["id"]
            )

        question = schemas.CreateQuestionSchema(
            question_id=question_dict["id"],
            question_text=question_dict["question"],
            answer_text=question_dict["answer"],
            created_at=question_dict["created_at"],
        )
        question_added = add_question_to_db(db=db, question=question)

    return question_added


@app.get("/quiz/api/v1.0/read_quiz_questions")
def read_questions_from_db(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Question).limit(limit).all()
