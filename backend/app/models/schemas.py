from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    score: int
    comment: str = None

    class Config:
        orm_mode = True
