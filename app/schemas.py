from pydantic import BaseModel, Field, AwareDatetime


class QuestionsRequestSchema(BaseModel):
    questions_num: int = Field(gt=0)


class CreateQuestionSchema(BaseModel):
    question_id: int = Field(gt=0)
    question_text: str = Field(min_length=1)
    answer_text: str = Field(min_length=1)
    created_at: AwareDatetime

    class Config:
        orm_mode = True
